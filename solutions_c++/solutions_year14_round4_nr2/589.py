#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:512777216")
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

typedef vector<int> VI;

VI v;

int get_eu(VI &a) {
	int n = a.size();
	int l = 0, r = n - 1;
	int res = 0;
	forn(st, n)  {
		int mnpos = l;
		forn(j, n) {
			if (j >= l && j <= r && a[j] < a[mnpos])
				mnpos = j;
		}
		if (mnpos - l < r - mnpos) {
			res += mnpos - l;
			while(mnpos != l) {
				swap(a[mnpos], a[mnpos - 1]);
				--mnpos;
			}
			l++;
		} else {
			res += r - mnpos;
			while(mnpos != r) {
				swap(a[mnpos], a[mnpos + 1]);
				++mnpos;
			}
			r--;
		}
	}
	return res;
}

map<int, int> mxp;

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int ttt;
	scanf("%d", &ttt);
	forn(tt, ttt) {
		int n;
		cin >> n;
		v.clear();
		v.resize(n);
		forn(i, n)
			cin >> v[i];
		int a[12346];
		forn(i, n)
			a[i] = v[i];
		sort(a, a + n);
		mxp.clear();
		forn(i, n)
			mxp[a[i]] = i;
		forn(i, n)
			v[i] = mxp[v[i]];
		int res = get_eu(v);
		
		printf("Case #%d: %d\n", tt + 1, res);
		cerr << (tt+1) << " test\n";
	}
}