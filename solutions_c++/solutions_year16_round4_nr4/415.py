#pragma comment(linker, "/STACK:66777216")
#define _CRT_SECURE_NO_WARNINGS
//#include <bits/stdc++.h>
//#include <unordered_set>
//#include <unordered_map>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <complex>
#include <cstring>
#include <cstdio>
#include <bitset>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#include <list>
#include <cmath>


//#define fi first
//#define se second

using namespace std;

#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define forn(i,n) for(int i = 0; i < (int)(n); ++ i)
#define for1(i,n) for(int i = 1; i <= (int)(n); ++ i)
#define fore(i,a,b) for(int i = (int)(a); i <= (int)(b); ++ i)
#define ford(i,n) for(int i = (int)(n)-1; i >= 0; -- i)
#define ford1(i,n) for(int i = (int)(n); i >= 1; -- i)
#define fored(i,a,b) for(int i = (int)(b); i >= (int)(a);--i)
#define mp make_pair 
#define pb push_back
#define sz(v) ((int)((v).size()))
#define all(v) (v).begin(), (v).end()

typedef std::vector<int> vi;
typedef std::vector<vi> vvi;
typedef std::pair<int,int> pii;
typedef std::vector<pii> vpi;
typedef long long LL;
typedef/* long*/ double LD;
//typedef unsigned long long ULL;

const int N = 25+3;
int n;
char s[ N ][ N ];

char c[ N ][ N ];

int a[ N ][ N ], m1, n1;

const int INF = N;
int vengerski(int n,int m){
	if(n==0)return 0;
	vector<int> u (n+1,0), v (m+1,0), p (m+1,0), way (m+1,0);
	for (int i=1; i<=n; ++i) {
		p[0] = i;
		int j0 = 0;
		vector<int> minv (m+1, INF);
		vector<char> used (m+1, false);
		do {
			used[j0] = true;
			int i0 = p[j0],  delta = INF,  j1;
			for (int j=1; j<=m; ++j)
				if (!used[j]) {
					int cur = a[i0][j]-u[i0]-v[j];
					if (cur < minv[j])
						minv[j] = cur,  way[j] = j0;
					if (minv[j] < delta)
						delta = minv[j],  j1 = j;
				}
			for (int j=0; j<=m; ++j)
				if (used[j])
					u[p[j]] += delta,  v[j] -= delta;
				else
					minv[j] -= delta;
			j0 = j1;
		} while (p[j0] != 0);
		do {
			int j1 = way[j0];
			p[j0] = p[j1];
			j0 = j1;
		} while (j0);
	}
	return v[0];
}
void solve(){
	int T;
	scanf("%d", &T);
	for1(it,T){
		scanf("%d", &n);
		forn(i,n)
			scanf("%s", s[i]);
		int res = n*n;
		forn(mask,1<<(n*n)){
			bool ok = true;
			forn(i,n){
				forn(j,n){
					c[i][j] = s[i][j];
					if(mask&(1<<(i*n+j))){
						c[i][j] = '1';
						if(s[i][j]=='1')
							ok = false;
					}
				}
			}
			if(ok){
				forn(u,n){
						int n1 = 0, m1 = 0;
						forn(j,n){
							if(c[u][j]=='1'){
								++ n1;
								m1 = 0;
								forn(i,n){
									if(i==u)continue;
									a[n1][++m1] = 0;
									if(c[i][j]=='1')
										a[n1][m1] = -1;
								}
							}
						}
					m1 = n-1;
					if(n1 <= m1 && vengerski(n1,m1)==n1){
						ok = false;
						break;
					}

				}
				if(ok){
					int q = 0;
					forn(i,n*n){
						if((1<<i)&mask)
							++ q;
					}
					if(res==-1 || res > q)
						res = q;
				}
			}
		}
		printf("Case #%d: %d\n", it, res);
	}
}

int u[ N ];
void testgen(){
	FILE * f = fopen("input.txt", "w");
	srand(time(NULL));
	int T = 100;
	fprintf(f, "%d\n", T);
	for1(it,T){
		int n = 200, k = 100;
		for1(i,n){
			u[i] = rand()%101;
		}
		fprintf(f, "%d %d\n", n, k);
		for1(i,n){
			fprintf(f, "%.2f ", u[i]/100.0);
		}
		fprintf(f, "\n");
	}
	fclose(f);
}

int main() {
#ifdef HOME
//	testgen();
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);

	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
#else
#define task "make-a-row"
	//		freopen("input.txt", "r", stdin);
	//		freopen("output.txt", "w", stdout);
//		freopen(task".in", "r", stdin);
//		freopen(task".out", "w", stdout);
#endif

	std::cout<<std::fixed;
	std::cout.precision(8);
	std::cerr<<std::fixed;
	std::cerr.precision(3);

	solve();

#ifdef HOME
	std::cerr<<"Execution time = "<<clock()/1000.0<<"ms\n";
#endif
	return 0;
}