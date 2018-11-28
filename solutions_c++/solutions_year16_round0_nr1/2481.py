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

int T;
//const int N = 1000000;
//int a[ N+10 ];
int b[ 100 ];
void solve(){
/*	int ma = 0;
	for1(i,N){
		LL x = i;
		forn(j,10)
			b[j] = 0;
		while(1){
			++ a[i];
			ma = max(ma,a[i]);
			if(a[i] > N){
				printf("%d\n", i);
			}
			LL y = x;
			while(y){
				b[ y%10 ] = 1;
				y/=10;
			}
			bool ok = true;
			forn(j,10)
				if(b[j]==0)
					ok = false;
			if(ok)break;
			x+=i;
		}
	}
	cout<<ma<<endl;*/
	scanf("%d", &T);
	for1(it,T){
		int n;
		scanf("%d", &n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n", it);
			continue;
		}
		LL x = n;
		forn(j,10)
			b[j] = 0;
		while(1){
			LL y = x;
			while(y){
				b[ y%10 ] = 1;
				y/=10;
			}
			bool ok = true;
			forn(j,10)
				if(b[j]==0)
					ok = false;
			if(ok)break;
			x+=n;
		}
		printf("Case #%d: %lld\n", it, x); 
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
	freopen("A-large.in", "r", stdin);
//	freopen("chess.txt", "r", stdin);
	freopen("A-large.out", "w", stdout);
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