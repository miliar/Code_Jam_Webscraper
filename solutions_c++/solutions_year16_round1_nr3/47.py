#pragma comment (linker, "/STACK:128000000")
#include <iostream> 
#include <cstdio> 
#include <fstream>
#include <functional>
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <stack> 
#include <cmath> 
#include <algorithm> 
#include <cstring> 
#include <bitset> 
#include <ctime> 
#include <sstream>
#include <stack> 
#include <cassert> 
#include <list> 
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef long long li;
typedef long long i64;
typedef pair <int, int> pi;
typedef vector <int> vi;
typedef double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();

//int timer = 0;
#define FILENAME ""

int main() {
	string s = FILENAME;
#ifdef YA
	//assert(!s.empty());
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//cerr<<FILENAME<<endl;
	//assert (s != "change me please");
	clock_t start = clock();
#else
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	//freopen(FILENAME ".in", "r", stdin);
	//freopen(FILENAME ".out", "w", stdout); 
	cin.tie(0);
#endif
	cout.sync_with_stdio(0);
	cout.precision(10);
	cout << fixed;
	int t = 1;

	cin >> t;
	for (int i = 1; i <= t; ++i) {
		//++timer;
		cout << "Case #" << i << ": ";
		solve();
	}
#ifdef YA
	cerr << "\n\n\n" << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n\n\n";
#endif
	return 0;
}

void solve() {
	int n;
	cin >> n;
	vector <int> f(n);

	for (int i = 0; i < n; ++i) {
		cin >> f[i];
		--f[i];
	}

	int best_ans = 0;

	vector <int> best_prev_end(n);

	for (int j = 0; j < n; ++j) {
		vector <int> used(n);

		int cur = j;

		vector <int> path;

		int len = 0;

		while (!used[cur]) {
			used[cur] = 1;
			++len;
			
			path.push_back(cur);

			cur = f[cur];
		}

		if (cur == j) {
			best_ans = max(best_ans, len);
		}
		if (cur == path[path.size() - 2]) {
			best_prev_end[cur] = max(best_prev_end[cur], len - 2);
		}
	}

	int pos_sum = 0;
	for (int j = 0; j < n; ++j) {
		if (f[f[j]] == j) {
			pos_sum++;
		}
	}

	for (int j = 0; j < n; ++j) {
		pos_sum += best_prev_end[j];
	}

	cout << max(pos_sum, best_ans) << "\n";
}