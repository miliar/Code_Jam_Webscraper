#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef int ret_t;

struct Group {
    ll time;
    int group;
    int cycle;
    int hiker;
};
class compare { // for queue
public:
    bool operator()(const Group & a, const Group & b) const {
	return a.time > b.time; // here > means lower first
    }
};

class Solver {
public:
    ret_t solve(int n, vector<int> d, vector<ll> h, vector<ll> m) {
	ret_t ret;
	//vector<int> over(n);
	int cur = 0;
	priority_queue<Group, vector<Group>, compare> q;
	for (int i = 0; i < n; ++i) {
	    //over[i] = h[i];
	    cur += h[i];
	    Group p;
	    p.group = i;
	    p.cycle = 0;
	    p.hiker = 0;
	    p.time = (ll)(360 - d[i]) * m[i];
	    q.push(p);
	}
	int neg = cur;
	ret = cur;
	while (true) {
	    Group p;
	    p = q.top();
	    q.pop();
	    //cerr << p.group <<'.'<< p.cycle<<'.'<< p.hiker << "\t= " << p.time<<endl;
	    if (p.hiker == 0) {
		Group np(p);
		np.cycle++;
		np.time += 360 * m[np.group];
		q.push(np);
	    }
	    if (p.hiker + 1 < h[p.group]) {
		Group np(p);
		np.hiker++;
		np.time += (np.cycle + 1) * 360 - d[np.group];
		q.push(np);
	    }

	    //over[p.group]++;
	    if (p.cycle == 0) {
		--neg;
		--cur;
	    }
	    else {
		++cur;
	    }
	    
	    if (p.time != q.top().time) {
		ret = min(ret, cur);
	    }

	    if (cur - neg >= ret) break;
	}
	return ret;
    }
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr //<< "Case "
	    << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        int n;
        {
            stringstream A(s);
            A >> n;
        }
	vector<int> d(n);
	vector<ll> h(n);
	vector<ll> m(n);
	for (int i = 0; i < n; ++i) {
	    getline(cin, s);
	    stringstream A(s);
	    A >> d[i] >> h[i] >> m[i];
	}
        ret_t ret = solver.solve(n, d, h, m);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
