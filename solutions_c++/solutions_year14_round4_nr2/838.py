#include "/Users/roman/Dev/SharedCpp/DebugOutput.h"
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <memory>
#include <sstream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <cassert>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (int)((s).end()-(s).begin())
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define ll long long
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define VI vector<int>
#define ppb pop_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())

void solve_sequential();
void solve_parallel(int thread_pool_size = 2);

class Solver {
  public:
  	void read();
  	void solve();
  	void output();
  	// <0> define data structures here
  	int n, ans;
  	vector<int> a;
};

void Solver::read() {
	// <1>
	cin >> n;
	a.assign(n, 0);
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
}

int calc(const vector<int> &p) {
	int ans = 0;
	for (int i = 0; i < p.size(); i++)
		for (int j = 0; j < i; j++)
			if (p[j] > p[i])
				ans++;
	return ans;
}

int brute(vector<int> p) {
	vector<int> q = p;
	SORT(q);
	map<int, int> miq;
	for (int i = 0; i < q.size(); i++) miq[q[i]] = i;
	for (int i = 0; i < p.size(); i++) p[i] = miq[p[i]];
	q = p;
	SORT(q);
	int ans = INF;
	do {
		bool ok = true;
		int mx = max_element(all(q)) - q.begin();
		for (int i = mx; i > 0; i--) 
			if (q[i] < q[i - 1]) ok = false;
		for (int i = mx; i < q.size() - 1; i++) 
			if (q[i] < q[i + 1]) ok = false;
		if (!ok) continue;
		vector<int> iq(q.size(), 0);
		for (int i = 0; i < q.size(); i++) iq[q[i]] = i;
		int now = 0;
		for (int i = 0; i < p.size(); i++) {
			now += abs(iq[p[i]] - i);
		}
		now /= 2;
		ans = min(ans, now);
	} while (next_permutation(all(q)));
	return ans;
} 

void Solver::solve() {
	// <2>
	ans = 0;
	for (int i = 0; i < n; i++) {
		int before = 0, after = 0;
		for (int j = 0; j < n; j++) {
			if (j < i) {
				if (a[j] > a[i]) before++;
			} else {
				if (a[j] > a[i]) after++;
			}
		}
		ans += min(before, after);
	}
}

void Solver::output() {
	// <3>
	cout << ans << endl;
}


int main(int argc, char *argv[])
{
    solve_sequential();
    //solve_parallel();
	return 0;
}

void solve_sequential() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout); 
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		clog << "solving... " << tc << endl;
		Solver *c = new Solver();
		c->read();
		c->solve();
	    printf("Case #%d: ", tc);
		c->output();
	}
}
#define entrylog(s, tc) {lock_guard<mutex> g(mlog); clog << s << tc << endl; }
string get_file_name(int tc) {
	char filename[2048];
	sprintf(filename, "cache/%03d", tc);
	return string(filename);
};
void solve_parallel(int thread_pool_size) {
    freopen("input.txt", "rt", stdin); 

    system("rm -r cache; mkdir cache;");

	int TC;
	scanf("%d", &TC);
	int active_solvers = 0;
	mutex mcv, minput, mlog, moutput;
	condition_variable cv;
	vector<thread> threads;
	for (int tc = 1; tc <= TC; tc++) {
		entrylog("Waiting for free worker... ", tc);
		{
			unique_lock<mutex> lk(mcv);
			cv.wait(lk, [active_solvers, thread_pool_size](){
				return active_solvers < thread_pool_size;
			});
		}
		entrylog("Got free worker... ", tc);
		threads.push_back(
			thread([tc, &mcv, &minput, &moutput, &mlog, &cv](){
			entrylog("Creating solver... ", tc);
			Solver *s = new Solver();
			entrylog("Wating for reading... ", tc);
			{
				lock_guard<mutex> lk(minput);
				s->read();
			}
			entrylog("Started solving... ", tc);
			s->solve();
			entrylog("Outputting result... ", tc);
			{
				lock_guard<mutex> lk(moutput);
				freopen(get_file_name(tc).c_str(), "wt", stdout);
				printf("Case #%d: ", tc);
				s->output();
			}
			{
				lock_guard<mutex> lk(mcv);
				entrylog("Erasing solver... ", tc);
				delete s;
				cv.notify_all();
			}
		}));
	}
	for (int i = 0; i < threads.size(); i++) {
		threads[i].join();
	}
	clog << "assembly" << endl;
	system("rm output.txt");
	for (int tc = 1; tc <= TC; tc++) {
		char command[2048];
		sprintf(command, "cat %s >> output.txt", get_file_name(tc).c_str());
		system(command);
	}
}