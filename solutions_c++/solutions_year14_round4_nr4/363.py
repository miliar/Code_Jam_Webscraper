#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);
const int size = 100;

int tc, n, m;

string str[size];
int cnt[size];
int best = 0;
int cntb = 0;
int cur[size];
set <string> allsubs[size];

void rec(int ps) {
	if (n == ps) {
		for (int i = 0; i < m; i++)
			if (cnt[i] == 0)
				return;
		for (int i = 0; i < m; i++)
			allsubs[i].clear();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= (int) str[i].size(); j++)
				allsubs[cur[i]].insert(string(str[i].begin(), str[i].begin() + j));
		}
		int val = 0;
		for (int i = 0; i < m; i++)
			val += allsubs[i].size();
		if (best < val) {
			best = val;
			cntb = 0;
		}
		if (best == val)
			cntb++;
		return;
	}

	for (int i = 0; i < m; i++) {
		cur[ps] = i;
		cnt[i]++;
		rec(ps + 1);
		cnt[i]--;
	}
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
    	cerr << tnum + 1 << endl;
    	cin >> n >> m;
    	for (int i = 0; i < n; i++)
    		cin >> str[i];
    	best = 0;
    	cntb = 0;
    	for (int i = 0; i < m; i++)
    		cnt[i] = 0;
    	rec(0); 

    	cout << "Case #" << tnum + 1 << ": " << best << ' ' << cntb << endl;
    }

    return 0;
}