#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define FOR(i, a, b) for (auto i = (a); i < (b); i++)
#define FORD(i, a, b) for (auto i = (b)-1; i >= (a); i--)
#define FORE(it, x) for (auto it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) (x).begin(), (x).end()

int main(void)
{
	//freopen("c:\\users\\gergely\\documents\\codejam\\3\\c0.in", "r", stdin);
	int tn;
	cin >> tn;
	FOR (ti, 1, tn+1) {
		cerr << ".";
		cout << "Case #" << ti << ": ";
		int n;
		cin >> n;
		vector<bool> moveenter(n);
		vector<int> movenum(n);
		set<int> all;
		FOR (i, 0, n) {
			char c;
			cin >> c >> movenum[i];
			moveenter[i] = c == 'E';
			if (movenum[i] > 0) all.insert(movenum[i]);
		}
		set<int> inside;
		set<int> seen;
		function<void(int k)> bt;
		int best = 10000;
		bt = [&](int k) {
			if (k == n) {
				best = min(best, (int)inside.size());
			} else {
				set<int> poss;
				if (movenum[k] == 0) {
					poss = all;
					for (int x : seen) poss.insert(x);
					if (poss.size() > 0) poss.insert(1+*(--poss.end()));
					else poss.insert(1);
				} else poss.insert(movenum[k]);
				for (int x : poss) {
					//cout << x << " ";
					bool nowseen = false;
					if (moveenter[k]) {
						if (inside.find(x) == inside.end()) {
							inside.insert(x);
							nowseen = seen.find(x) == seen.end();
							if (nowseen) seen.insert(x);
							bt(k+1);
							inside.erase(x);
							if (nowseen) seen.erase(x);
						}
					} else {
						if (inside.find(x) != inside.end()) {
							inside.erase(x);
							bt(k+1);
							inside.insert(x);
						} else if (seen.find(x) == seen.end()) {
							seen.insert(x);
							bt(k+1);
							seen.erase(x);
						}
					}
				}
				//cout << endl;
			}
		};
		bt(0);
		if (best < 10000) cout << best << endl;
		else cout << "CRIME TIME" << endl;
	}
	return 0;
}
