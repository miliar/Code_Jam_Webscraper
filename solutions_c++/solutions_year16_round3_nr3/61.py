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
typedef long double LD;


int J, P, S, K;
void solve(){
	int T = 0;
	scanf("%d", &T);
	for1(it,T){
		scanf("%d%d%d%d", &J, &P, &S, &K);
		vi rJ, rP, rS;
		if(K >= S){//good
			for1(j,J)
				for1(p,P)
					for1(s,S){
						rJ.push_back( j );
						rP.push_back( p );
						rS.push_back( s );
					}
		}else
			if(K >= P){
				for1(j,J)
					for1(p,P)
						for1(s,K){
							rJ.push_back( j );
							rP.push_back( p );
							rS.push_back( s );
						}
			}else
				if(K >= J){//K < P <= S//solved
					forn(j,J){
						forn(p,P){
							for(int s = p; s < p+K; ++ s){
								rJ.push_back( j+1 );
								rP.push_back( p+1 );
								rS.push_back( s%P+1 );
							}
						}
					}
				}else{
					forn(j,J){
						forn(p,P){
							for(int k = 0; k < K; ++ k){
								rJ.push_back( j+1 );
								rP.push_back( p+1 );
								rS.push_back( (j+p+k)%P+1 );
							}
						}
					}
				}
		//K <= S
		printf("Case #%d: %d\n", it, sz(rJ));
		forn(i,sz(rJ)){
			printf("%d %d %d\n", rJ[i], rP[i], rS[i]);
		}
	}
}

void testgen(){
	FILE * f = fopen("input.txt", "w");
//	srand(time(NULL));
	fclose(f);
}

int main() {
#ifdef HOME
//	testgen();
//	freopen("input.txt", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
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