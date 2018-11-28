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
int n, R, P, S;
const int M = 12+3;
const int N = (1<<12)+10;

string s[ M ][ 3 ];
int q[ M ][ 3 ][ 3 ];
/*
bool check(int n, int P, int R, int S){
		a[0] = P;
		a[1] = R;
		a[2] = S;
		for(int i = 0; i < 3; ++ i){
			forn(j,3)
				b[j] = 0;
			b[i] = 1;
			for(int u = 1; u <= n; ++ u){
				forn(j,3)
					q[j] = b[j]+b[(j+2)%3];
				forn(j,3)
					b[j] = q[j];
			}
			bool ok = true;
			forn(j,3)
				if(b[j]!=a[j])
					ok = false;
			if(ok)
				return true;
		}
}*/
char ch[] = {'P', 'R', 'S'};
void init(){
	forn(i,3)
		s[0][i]+=ch[i];
	for(int n = 1; n <= 12; ++ n){
		forn(i,3){
			if(s[n-1][i] < s[n-1][(i+2)%3])
				s[n][i] = s[n-1][i] + s[n-1][(i+2)%3];
			else
				s[n][i] = s[n-1][(i+2)%3]+s[n-1][i];
		}
	}
	for(int n = 0; n <= 12; ++ n){
		forn(i,3){
			forn(j,sz(s[n][i])){
				forn(u,3){
					if(s[n][i][j]==ch[u])
						++q[n][i][u];
				}
			}
		}
	}
}
int a[3];
char c[ N ];
void solve(){
	init();
	int T = 0;
	scanf("%d", &T);
	for1(it,T){
		scanf("%d%d%d%d", &n, &R, &P, &S);
		a[0] = P;
		a[1] = R;
		a[2] = S;
		string res;
		forn(i,3){
			bool ok = true;
			forn(j,3){
				if(a[j]!=q[n][i][j])
					ok = false;
			}
			if(ok){
				if(sz(res)==0 || res > s[n][i])
					res = s[n][i];
			}
		}
		//memset(s,0,sizeof s);
		forn(i,sz(res))
			c[i] = res[i];
		c[sz(res)] = 0;
		printf("Case #%d: ", it);
		if(!sz(res)){
			printf("IMPOSSIBLE\n");
		}else{
			printf("%s\n", c);
		}
	}
}

void testgen(){
	FILE * f = fopen("input.txt", "w");
	srand(time(NULL));
//	int T = 1;
//	fprintf(f, "%d\n", T);
	fclose(f);
}

int main() {
#ifdef HOME
//	testgen();
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#else
#define task "make-a-row"
	//		freopen("input.txt", "r", stdin);
	//		freopen("output.txt", "w", stdout);
//		freopen(task".in", "r", stdin);
//		freopen(task".out", "w", stdout);
#endif

	std::cout<<std::fixed;
	std::cout.precision(9);
	std::cerr<<std::fixed;
	std::cerr.precision(3);

	solve();

#ifdef HOME
	std::cerr<<"Execution time = "<<clock()/1000.0<<"ms\n";
#endif
	return 0;
}