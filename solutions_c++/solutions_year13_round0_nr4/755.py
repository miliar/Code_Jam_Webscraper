#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <math.h>
#include <queue>
#include <memory.h>
#include <iostream>
#include <stack>
#include <complex>
#include <list>

using namespace std;
 
void ASS(bool b)
{
    if (!b)
    {
        ++*(int*)0;
    }
}
 
#define FOR(i, x) for (int i = 0; i < (int)(x); ++i)
#define CL(x) memset(x, 0, sizeof(x))
#define CLX(x, y) memset(x, y, sizeof(x))
 
#pragma comment(linker, "/STACK:106777216")
 
typedef vector<int> vi;

typedef unsigned long long LL;

int n;
char d[1 << 20];
char w[1 << 20];
vi g[556];

int okeys[556];
int keys[556];

map<int, int> mp;

int renumber(int x) {
	int &t = mp[x];
	if (!t)
		t = mp.size();
	return t;
}

bool D(int m) {
	if (m == (1 << n) - 1)
		return 1;
	char& res = d[m];
	if (res)
		return res - 1 != 0;
	res = 0;
	FOR(i, n) {
		if (((m >> i ) & 1) == 0 && keys[okeys[i]] > 0) {
			keys[okeys[i]]--;
			FOR(j, g[i].size())
				keys[g[i][j]]++;
			if (D(m + (1 << i))) {
				res = 1;
				w[m] = i;
				break;
			}
			FOR(j, g[i].size())
				keys[g[i][j]]--;
			keys[okeys[i]]++;
		}
	}
	res++;
	return res - 1 != 0;
}

void W(int m) {
	if (m == (1 << n) - 1)
		return;
	if (m)
		cout << " ";
	cout << (int)(w[m] + 1);
	W(m + (1 << w[m]));
}

void Solve() {
	mp.clear();
	CL(keys);
	CL(okeys);
	CL(d);
	int k;
	cin >> k >> n;
	FOR(i, n)
		g[i].clear();

	FOR(i, k) {
		int x;
		cin >> x;
		x = renumber(x);
		keys[x]++;
	}
	FOR(i, n) {
		int x;
		cin >> x;
		x = renumber(x);
		okeys[i] = x;
		cin >> k;
		FOR(j, k) {
			cin >> x;
			x = renumber(x);
			g[i].push_back(x);
		}
	}
	if (!D(0)) {
		cout << "IMPOSSIBLE";
		return;
	} else {
		W(0);
	}
}

int main()
{
	freopen("c://my//in.txt", "r", stdin);
	freopen("c://my//out.txt", "w", stdout);

	int t;
	cin >> t;
	FOR(i, t) {
		cout << "Case #" << (i + 1) << ": ";
		Solve();
		cout << "\n";
	}

	return 0;
}
