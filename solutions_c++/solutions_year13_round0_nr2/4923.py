#pragma warning(disable : 4996)
#include <cstdio>
#include <cmath>
#include <ctime>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <string>
using namespace std;
typedef std::vector<int> vi;
typedef std::vector<vi> vvi;
typedef std::pair<int,int> ii;
typedef std::vector<ii> vii;
typedef std::vector<string> vs;
typedef std::vector<double> vd;

#define sz(a) int(a.size())
#define REP(i,n) for(int i = 0; i < n; ++i)
#define FOR(i,a) for(int i = 0; i < sz(a); ++i)

inline bool isdig(int a){return unsigned(a-'0') < 10;}
template<class T> static inline T getnum(){
   unsigned i; T j;
   do i = getchar(); while(!isdig(i));
   j = i-'0';  i=getchar() ;
   while(isdig(i)){ j = (j<<1)+(j<<3)+(i-'0'); i = getchar(); }
   return j;
}

int N, T;

int L[101][101], MR[101],MC[101];
int main(int argc, char *argv[]){
	bool out = true;
	#ifndef ONLINE_JUDGE
		FILE *F = fopen("Bb.txt","r");
		freopen("Bb.txt","r",stdin);
		if( out){
			freopen("Out.txt","w",stdout);
		}
	#endif
	int NTST;
	scanf("%d\n",&NTST);
	for( int tst = 0; tst < NTST; ++tst){
		int N,M;
		scanf("%d %d\n",&N, &M);
		for(int r = 0; r < N; ++r) MR[r] = 0;
		for(int c = 0; c < M; ++c) MC[c] = 0;

		for(int r = 0; r < N; ++r){
			for(int c = 0; c < M; ++c){
				scanf("%d ",&L[r][c]);
				if( L[r][c] > MR[r] ) MR[r] = L[r][c];
				if( L[r][c] > MC[c] ) MC[c] = L[r][c];
			}
		}
		bool ok = true;
		for(int r = 0; r < N; ++r){
			for(int c = 0; c < M; ++c){
				if( L[r][c] < MR[r] && L[r][c] < MC[c] )
					ok = false;
			}
		}
		printf("Case #%d: ", tst+1);
		if( ok){
			printf( "YES\n" );
		} else {
			printf( "NO\n" );
		}
	}

	return 0;
}
