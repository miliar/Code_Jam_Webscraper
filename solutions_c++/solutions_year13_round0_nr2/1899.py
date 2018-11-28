
//{{{
#define DEF
#ifdef DEF
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <stack>
#include <vector>
#include <list>
#include <map>
#include <cctype>
#include <queue>
#include <cstring>
#include <cmath>
#include <set>
#include <deque>


//-----------------------------------------------------


using namespace std;
typedef unsigned int uint;
typedef long long int llint;
typedef unsigned long long int ullint;

typedef pair<int,int> Pii;
typedef pair<llint,llint> Pll;

#define mrepp(i,n,x)  for(int i = n-1; i >= x; i--)
#define mrep(i,n) mrepp(i,n,0)
#define repp(i,x,n)  for(int i = x; i < n; i++)
#define rep(i,n) repp(i,0,n)
#define pb        push_back
#define all(vec)  (vec).begin(),(vec).end()
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
//#define reach(i,c) for(__typeof((c).rbegin()) i=(c).rbegin();i!=(c).rend();i++)
#define fst         first
#define scd         second

#define sz(v)     ((llint)(v).size())
//#define bit(n)    (1ll<<(li)(n))
//#define mkP        make_pair

//-----------------------------------------------------
#endif
//}}}

int h[110][110];
int max_n[110];
int max_m[110];

int N,M,T;

int main(){
	cin >> T;
	rep(t,T){
		cin >> N >> M;
		rep(n,N) rep(m,M) cin >> h[n][m];
		
		//cout << N << ' ' << M << endl;
		//rep(n,N){rep(m,M) cout << h[n][m] << ' '; cout << endl;}
		
		rep(i,max(N,M)) max_n[i] = max_m[i] = 0;
		rep(n,N) rep(m,M){
			max_n[m] = max(max_n[m],h[n][m]);
			max_m[n] = max(max_m[n],h[n][m]);
		}
		
		//rep(i,N) cout << max_m[i] << (i+1==N?'\n':' ');
		//rep(i,M) cout << max_n[i] << (i+1==M?'\n':' ');
		
		bool ans = true;
		rep(n,N) rep(m,M)
			if( h[n][m] < max_n[m] && h[n][m] < max_m[n] ) ans = false;
		
		printf("Case #%d: ",t+1);
		cout << (ans?"YES":"NO") << endl;
		
	}
	return 0;
}
