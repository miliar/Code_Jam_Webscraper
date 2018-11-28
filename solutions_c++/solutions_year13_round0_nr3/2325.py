#include <tr1/unordered_map>
#include <set>
#include <list>
#include <stack>
#include <cmath>
#include <queue>
#include <ctime>
#include <cfloat>
#include <vector>
#include <string>
#include <cstdio>
#include <bitset>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iomanip>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;
using namespace tr1;

#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define RFOR(i, b, a) for(int i = b; i >= a; --i)
#define REP(i, N) for(int i = 0; i < N; ++i)
#define RREP(i, N) for(int i = N-1; i >= 0; --i)
#define FORIT(i, a) for( TI(a) i = a.begin(); i != a.end(); i++ )
#define MAXN 10000
#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3FFFFFFFFFLL
#define FILL(X, V) memset( X, V, sizeof(X) )
#define TI(X) __typeof((X).begin())
#define ALL(V) V.begin(), V.end()
#define SIZE(V) int((V).size())
#define pb push_back
#define mp make_pair

struct tri{
	int ant, novo;
	tri ( int ant = 0, int novo = 0) : ant(ant), novo(novo) { }
};

int n, m;
typedef vector < int > vi;
typedef vector < vi > vii;
typedef vector < tri > vtri;
typedef vector < vtri > vvtri;
typedef long long int64;
typedef unsigned long long uint64;

int x[] = {-1,-1,-1, 0, 1, 1, 1, 0 };
int y[] = {-1, 0, 1, 1, 1, 0,-1,-1 };

unordered_map < uint64 , int > vet;
unordered_map < uint64 , int > :: iterator it;
vector < uint64 > lim;

bool eh(uint64 x ){
	char str[100];
	sprintf(str, "%lld", x);
	int tam = strlen(str);
	for(int i = 0, j = tam-1; i <= j; i++, j--) if( str[i] != str[j] ) return false;
	return true;
}

void process( ){
	for(uint64 i = 0; i < 10000010; i++) if( eh( i ) && eh( i * i ) ) lim.pb(i*i);
	sort(ALL(lim));
}

int solve(uint64 a, uint64 b){
	int ans = 0;
	REP(i,lim.size()) if( lim[i] >= a && lim[i] <= b ) ans++;
	/*for( int i = 0, j = lim.size()-1; i <= j; i++, j--){
		if( lim[i] >= a && lim[i] <= b ) ans++;
		if( i == j ) continue;
		if( lim[j] >= a && lim[j] <= b ) ans++;
	}*/
	return ans;
}

int main(){
	ios::sync_with_stdio(false);
	int t, caso = 1;
	cin >> t;
	process();
	uint64 a, b;
	while( t-- ){
		cin >> a >> b;
		int ans = solve(a,b);
		cout << "Case #" << caso++ << ": " << ans << "\n";
	}
	return 0;
}
