#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXN 100001
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define mp make_pair


string s[12];

int ts[5];
string t[5][12];

int same(string a, string b) {
	int i = 0;
	while(i < a.size() && i < b.size() && a[i] == b[i])
		++i;
	return i;
}

int go(int ser) {
	int c = 1;
	forn(i, ts[ser]) {
		string st = t[ser][i];
		int maxp = 0;
		forn(j, i) {
			maxp = max(maxp, same(st, t[ser][j]));
		}
		c += st.size() - maxp;
	}
	return c;
}

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int ttt;
	scanf("%d", &ttt);
	forn(tt, ttt) {
		int m, n;
		cin >> m >> n;
		forn(i, m) 
			cin >> s[i];

		int pw = 1;
		int mx = 0, cnt = 1;
		forn(i, m)
			pw *= n;
		forn(mask, pw) {
			memset(ts, 0, sizeof (ts));
			int msk = mask;
			forn(i, m) {
				int serv = msk % n;
				t[serv][ts[serv]++] = s[i];
				msk /= n;
			}
			int ok = 1;
			forn(i, n) {
				if (!ts[i])
					ok = 0;
			}
			if (!ok)
				continue;
			int get = 0;
			forn(i, n) {
				get += go(i);
			}
			if (get > mx) {
				mx = get;
				cnt = 1;
			} else {
				if (get == mx)
					++cnt;
			}
		}
		
		printf("Case #%d: %d %d\n", tt + 1, mx, cnt);
	}
}