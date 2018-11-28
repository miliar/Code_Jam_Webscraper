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

const int N = 28;
int n;
int p[ N ];
char s[ N ];
void solve(){
	int T = 0;
	scanf("%d", &T);
	for1(it,T){
		scanf("%d", &n);
		for1(i,n)
			scanf("%d", &p[i]);
		printf("Case #%d:", it);
		while(1){
			pair<pii,pii> ma = mp(mp(0,0),mp(0,0));
			int S = 0;
			for1(i,n){
				S+=p[i];
				if(ma.first <= mp(p[i],i)){
					swap(ma.first,ma.second);
					ma.first = mp(p[i],i);
				}else{
					ma.second = max(ma.second,mp(p[i],i));
				}
			}
			int top = 0;
			if(ma.first.first==0)break;

			int val = ma.second.first;
			if(2*val > S-1){
				--p[ ma.first.second ];
				--p[ ma.second.second ];
				printf(" %c%c", (char)(ma.first.second-1+'A'),(char)(ma.second.second-1+'A'));
			}else{
				--p[ ma.first.second ];
				printf(" %c", (char)ma.first.second-1+'A');
			}
		}
		puts("");
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
	std::cout.precision(8);
	std::cerr<<std::fixed;
	std::cerr.precision(3);

	solve();

#ifdef HOME
	std::cerr<<"Execution time = "<<clock()/1000.0<<"ms\n";
#endif
	return 0;
}