#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a);i<(int)(b);++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(x) (x).begin(),(x).end()
#define pb push_back

using namespace std;

typedef int64_t ll;
typedef long double ld;

const int INF = 1e9;
const double EPS = 1e-13;

template<class T> T &chmin(T &a, const T &b) { return a = min(a, b); }
template<class T> T &chmax(T &a, const T &b) { return a = max(a, b); }

#define fi first
#define se second
typedef pair<double,double> P;

int n;
double v , x;
double r[128], c[128];
vector<P> s;

bool f( double t ){
  double low = 0.0;
  double am = 0.0;
  REP( i , n ){
    if( am+t*s[i].se <= v ){
      am += t*s[i].se;
      low += t*s[i].se*s[i].fi;
    } else {
      low += (v-am)*s[i].fi;
      am += v-am;
    }
  }

  double high = 0.0;
  am = 0.0;
  for( int i = n-1; i >= 0; i-- ){
    if( am+t*s[i].se <= v ){
      am += t*s[i].se;
      high += t*s[i].se*s[i].fi;
    } else {
      high += (v-am)*s[i].fi;
      am += (v-am);
    }    
  }

  
  return low - EPS <= v*x && v*x <= high + EPS;
}

int main(){

  int tc;
  cin >> tc;

  FOR( cnt , 1 , tc+1 ){
    cin >> n >> v >> x;
    REP( i , n )
      cin >> r[i] >> c[i];

    s.clear();
    REP( i , n )
      s.pb( P( c[i] , r[i] ) );
    sort( ALL( s ) );

    if( n == 1 ){
      if( s[0].fi - EPS < x && x < s[0].fi + EPS ){
	
      } else {
	cout << "Case #" << cnt << ": ";
	cout << "IMPOSSIBLE" << endl;
	continue;
      }
    }
    
    if( n == 2 ){
      if( ( s[0].fi+EPS < x && s[1].fi+EPS < x ) || (s[0].fi>x+EPS && s[1].fi>x+EPS )){
	cout << "Case #" << cnt << ": ";
	cout << "IMPOSSIBLE" << endl;
	continue;
      }
    }
    
    double lb = 0.0, ub = 1e9;
    REP( loop , 300 ){
      double md = (lb+ub)/2.0;
      if( f(md) ) ub = md;
      else lb = md;
    }


    cout << "Case #" << cnt << ": ";
    if( ub > 5*(1e8) ) cout << "IMPOSSIBLE" << endl;
    else cout << fixed << setprecision( 18 ) << ub << endl;
  }
  
  return 0;
}
