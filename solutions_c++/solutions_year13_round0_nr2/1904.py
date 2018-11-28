#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#pragma comment(linker, "/STACK:200000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <iomanip>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <iomanip>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

#define pb push_back
#define mp make_pair
#define mset(mas,val) memset(mas,val,sizeof(mas))
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
	
const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;

int main(){
#ifdef gridnevvvit
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
	int testcases, testcount = 1;
	cin >> testcases;
	while(testcases--) {
		printf("Case #%d: ", testcount++);
		int n, m;
		cin >> n >> m;
		vector < vector < int > > d(n, vector < int > (m, 0));
		forn(i,n) {
			forn(j,m) {
				cin >> d[i][j];
			}
		}
		vector < int > used1(n, 0);
		vector < int > used2(m, 0);
		while(true) {
			bool relax = false;
			int Mmin = 200;
			forn(i, n) {
				forn(j, m) {
					if (!used1[i] && !used2[j])
						Mmin = min(Mmin, d[i][j]);
				}
			}
			forn(i,n) {
				if (used1[i])
					continue;
				bool check = true;
				vector < int > tt;
				forn(j, m) {
					if (!used2[j]) 
						tt.pb(d[i][j]);
				}
				forn(j, sz(tt)) {
					if (tt[j] != tt[0])
						check = false;
				}
				if (check && sz(tt) > 0 &&tt[0] == Mmin) {
					used1[i] = true;
					relax = true;
				}
			}
			Mmin = 200;
			forn(i, n) {
				forn(j, m) {
					if (!used1[i] && !used2[j])
						Mmin = min(Mmin, d[i][j]);
				}
			}
			forn(j, m) {
				if (!used2[j]) {
					bool check = true;
					vector < int > tt;
					forn(i,n) {
						if (!used1[i])
							tt.pb(d[i][j]);
					}
					forn(j, sz(tt)) {
						if (tt[j] != tt[0])
							check = false;
					}
					if (check && sz(tt) > 0 &&tt[0] == Mmin) 
						used2[j] = true, relax = true;
				}
			}
			if (!relax)
				break;
		}
		bool total1 = true, total2 = true;
		forn(i,n)
			if (!used1[i])
				total1 = false;
		forn(j,m)
			if (!used2[j])
				total2 = false;
		if (total1 || total2)
			puts("YES");
		else
			puts("NO");
	}
}