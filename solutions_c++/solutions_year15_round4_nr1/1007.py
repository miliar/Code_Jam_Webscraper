#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a);i<(int)(b);++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(x) (x).begin(),(x).end()
#define pb push_back

using namespace std;

typedef int64_t ll;
typedef long double ld;

const int INF = 1e9;
const ld EPS = 1e-11;

template<class T> T &chmin(T &a, const T &b) { return a = min(a, b); }
template<class T> T &chmax(T &a, const T &b) { return a = max(a, b); }

const int dx[] = { 1 , 0 , -1 , 0 };
const int dy[] = { 0 , -1 , 0 , 1 };

string s[128];

char cti( char c ){
  if( c == '>' ) return 0;
  if( c == '^' ) return 1;
  if( c == '<' ) return 2;
  if( c == 'v' ) return 3;
}

int r , c;

bool isin( int y , int x ){
  return 0 <= y && y < r && 0 <= x && x < c;
}


int main(){

  int tc;
  cin >> tc;

  FOR( cnt , 1 , tc+1 ){
    cin >> r >> c;
    REP( i , r )
      cin >> s[i];

    bool imp = false;
    int ans = 0;
    REP( i , r ){
      REP( j , c ){
	if( s[i][j] != '.' ){
	  int d = cti( s[i][j] );
	  bool ok = false;
	  int y = i+dy[d];
	  int x = j+dx[d];
	  while( isin( y , x ) ){
	    if( s[y][x] != '.' ) ok = true;
	    y += dy[d];
	    x += dx[d];
	  }
	  if( ok ) continue;
	  int co = 0;
	  REP( k , r )
	    if( s[k][j] != '.' ) co++;
	  REP( k , c )
	    if( s[i][k] != '.' ) co++;
	  if( co == 2 ) imp = true;
	  ans++;
	}
      }
    }

    if( imp ) cout << "Case #" << cnt << ": IMPOSSIBLE" << endl;
    else cout << "Case #" << cnt << ": " << ans << endl;
  }
  
  return 0;
}
