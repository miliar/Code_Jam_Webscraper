#include <algorithm>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <stdio.h>
#include <bitset>
#include <iterator>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define mp make_pair
#define pb push_back

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const double pi = acos(-1.0);
const int inf = (int) 1e9;

int c[10005];

int get(char cc) {
	if (cc == 'i') {
		return 2;
	}
	if (cc == 'j') {
		return 3;
	} else {
		return 4;
	}
}

int xx[5][5] = { 
	{0,0,0,0,0},
	{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1},
};

void go(int n, VI &a) {
	int now = c[0];
	a[0] = now;
	REP(i,1,n) {
		int bf = now;
		now = xx[abs(now)][c[i]];
		if (bf < 0) {
			now = -now;
		}
		a[i] = now;
	}
}

void go2(int n, VI &a) {
	REP(j,0,n) {
		int now = 1;
		REP(i,j,n) {
			int bf = now;
			now = xx[abs(now)][c[i]];
			if (bf < 0) {
				now = -now;
			}			
		}
		a[j] = now;
	}
}

int main()
{
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
    //freopen("i.in","r",stdin);
    //freopen("i.out","w",stdout);
#endif
	int T;
	cin >> T;
	FOR(TT,T) {
		if (TT) {
			cout << "\n";
		}
		cout << "Case #" << TT + 1 << ": ";
		cerr << TT << "\n";
		int l,x;
		cin >> l >> x;
		string s;
		cin >> s;
		FOR(i,x) {
			FOR(j,l) {
				c[i * l + j] = (get(s[j]));
			}
		}
		int n = l * x;
		VI a(n);
		go(n, a);
		VI b(n);
		go2(n, b);
		bool check = false;
		FOR(i,n - 1) {
			if (a[i] != 2) {
				continue;
			}
			int now = 1;
			REP(j,i + 1,n - 1) {
				int bf = now;
				now = xx[abs(now)][c[j]];
				if (bf < 0) {
					now = -now;
				}
				if (now == 3 && b[j + 1] == 4) {
					check = true;
					break;
				}
			}
			if (check) {
				break;
			}
		}
		if (check) {
			cout << "YES";
		} else {
			cout << "NO";
		}
	}
    return 0;
}