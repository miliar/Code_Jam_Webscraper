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

const int N = 200+5;
int n, k;
LD p[ N ];

LD a[ N ];

LD dp[ N ][ N ];
LD solvefor(){
	dp[0][0] = 1.0;
	for1(i,k){
		forn(j,i+1){
			dp[i][j] = dp[i-1][j]*(1.0-a[i]);
			if(j)
				dp[i][j] += dp[i-1][j-1]*a[i];
		}
	}
	return dp[k][k/2];
}
LD res;
bool mark[ N ];
int in[ N ];
const LD ep = 1e-9;
void solve(){
	int T = 0;
	cin>>T;
	for1(it,T){
		cin>>n>>k;
		for1(i,n){
			cin>>p[i];
//			if(p[i] < 0.5001)
//				p[i] = 1.0-p[i];
		}
		sort(p+1,p+n+1);
		cout<<"Case #"<<it<<": ";
		for1(i,n){
			in[i] = 0;
			mark[i] = 0;
		}
		for1(i,k){
			in[i] = i;
			a[i] = p[i];
			mark[i] = 1;
		}
		res = solvefor();
		while(1){
			bool ok = false;
			ford1(i,n){
				if(mark[i]==1 && i+1 <= n && mark[i+1]==0){
					a[ in[i] ] = p[i+1];
					LD res2 = solvefor();
					if(res2 > res-ep){
						res = res2;
						mark[i] = 0;
						mark[i+1] = 1;
						in[i+1] = in[i];
						ok = true;
						break;
					}else
						a[in[i]] = p[i];
				}
			}
			if(!ok)break;
		}
		cout<<res<<endl;
		cerr<<it<<endl;
/*		int t = k/2;
		for1(i,t){
			a[i] = p[i];
		}
		for(int i = n-t+1; i <= n; ++ i){
			a[i-(n-t)+t] = p[i];
		}
		cout<<solvefor()<<endl;*/
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

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
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