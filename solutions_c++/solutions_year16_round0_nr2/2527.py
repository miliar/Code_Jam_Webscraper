#pragma comment(linker, "/STACK:66777216")
#define _CRT_SECURE_NO_WARNINGS
//#include <bits/stdc++.h>
//#include <unordered_set>
//#include <unordered_map>
#include <functional>
#include <algorithm>
#include <iostream>
//#include <sstream>
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
//#define fi first
//#define se second

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
typedef vector<ld> vd;
typedef pair<ld,ld> pdd;
typedef vector<pdd> vpd;
typedef long long LL;
typedef long double LD;

const int  M = 10;
const int N = (1<<M)+10;
//int d[ M+2 ][ N ];
int T;
char s[ 10000 ];
void solve(){
/*	for1(n,M){
		forn(i,1<<n)
			d[n][i] = -1;
		
		queue<int> qu;
		d[n][0] = 0;
		qu.push( 0 );
		while(!qu.empty()){
			int v = qu.front();
			qu.pop();
			for(int q = 1; q <= n; ++ q){
				int u = v&((1<<q)-1);
				int t = v-u;
				u = u^((1<<q)-1);
				forn(j,q)
					if(u&(1<<j))
						t+=(1<<(q-1-j));
				if(d[n][t]==-1){
					d[n][t] = d[n][v]+1;
					qu.push(t);
				}
				//v
			}
		}
	}
	*/

	scanf("%d", &T);
	for1(it,T){
		scanf("%s", s);
		int m = strlen(s);
		int t = 0;
		forn(i,m)
			if(s[i]=='-')
				t+=(1<<i);
		int q = 0;
		ford(i,m){
			if(s[i]=='-'){
				int j = -1;
				while(j+1 < i && s[j+1]=='+')
					++ j;
				if(j!=-1){
					++ q;
					forn(u,j+1)
						s[u] = '-';
				}
				++ q;
				forn(u,i+1){
					if(s[u]=='+')
						s[u]='-';
					else
						s[u]='+';
				}
				reverse(s,s+i+1);
			}
		}
		printf("Case #%d: %d\n", it, q);
/*		if(q!=d[m][t]){
			printf("%s\n", s);
			printf("%d %d\n", q, d[m][t]);
			break;
		}*/
	}
}

void testgen(){
	FILE * f = fopen("input.txt", "w");
	//	srand(time(NULL));
	int T = 1<<M;
	fprintf(f, "%d\n", T);
	forn(i,T){
		forn(j,M){
			if((1<<j)&i)
				fprintf(f, "-");
			else
				fprintf(f, "+");
		}
		fprintf(f, "\n");
	}
	fclose(f);
}

int main() {
#ifdef HOME
//	testgen();
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#else
#define task "make-a-row"
	//		freopen("input.txt", "r", stdin);
	//		freopen("output.txt", "w", stdout);
//		freopen(task".in", "r", stdin);
//		freopen(task".out", "w", stdout);
#endif

	cout<<fixed;
	cout.precision(13);
	cerr<<fixed;
	cerr.precision(3);

	solve();

#ifdef HOME
	cerr<<"Execution time = "<<clock()/1000.0<<"ms\n";
#endif
	return 0;
}