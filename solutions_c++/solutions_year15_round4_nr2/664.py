//bcw0x1bd2 {{{
#include<bits/stdc++.h>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define MC(n,m) memcpy((n),(m),sizeof(n))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define FOR(x,y) for(__typeof(y.begin())x=y.begin();x!=y.end();x++)
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
#ifdef ONLINE_JUDGE
#define FILEIO(name) \
  freopen(name".in", "r", stdin); \
  freopen(name".out", "w", stdout);
#else
#define FILEIO(name)
#endif

void RI() {}

template<typename... T>
void RI( int& head, T&... tail ) {
	    scanf("%d",&head);
			    RI(tail...);
}

mt19937 rng(0x5EED);
int randint(int lb, int ub) {
    return uniform_int_distribution<int>(lb, ub)(rng);
}
// Let's Fight! }}}

#define double long double
typedef pair<double,double> pdd;

const double EPS = 1e-12;

int N;
double V,X;
pdd ip[105];


void input(){
  cin >> N >> V >> X;
  for (int i=0; i<N; i++){
    cin >> ip[i].F >> ip[i].S;
  }
}
void solve(int t){
 /*
  if (t != 40 && t != 88) return;
  if (t == 40 || t == 88){
    cout << V << " " << X << endl;
    for (int i=0; i<N; i++)
      cout << ip[i].F << " " << ip[i].S << endl;
  }
 */
  if (N == 1){
    if (fabs(ip[0].S - (double)X) < EPS){
      cout << "Case #" << t << ": " << (double)V/ip[0].F << endl;
    } else {
      cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }
  }
  if (N == 2){
    double a = ip[0].F;
    double b = ip[1].F;
    double c = ip[0].F * ip[0].S;
    double d = ip[1].F * ip[1].S;
    double e = V;
    double f = V * X;
    double mom = (a * d - c * b);
    if (fabs(mom) > EPS){
      double x = (e*d - b*f) / mom;
      double y = (a*f - e*c) / mom;
      if (x < -EPS || y < -EPS){
        if (fabs(ip[0].S-X) < EPS || fabs(ip[1].S-X) < EPS){
          x = 1e15;
          if (fabs(ip[0].S-X) < EPS)
            x = min(x, V / ip[0].F);
          if (fabs(ip[1].S-X) < EPS)
            x = min(x, V / ip[1].F);
          cout << "Case #" << t << ": " << x << endl;
        } else {
          cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        }
      } else {
        cout << "Case #" << t << ": " << max(x,y) << endl;
      }
    } else {
      if (fabs(a*f - c*e) < EPS){
        c = 1;
        d = -1;
        f = 0;
        mom = (a*d - c*b);
        double x = (d*e - b*f) / mom;
        double y = (a*f - e*c) / mom;
        if (x < -EPS || y < -EPS){
          if (fabs(ip[0].S-X) < EPS || fabs(ip[1].S-X) < EPS){
            x = min(e/b,e/a);
            if (fabs(ip[0].S-X) < EPS)
              x = min(x, V / ip[0].F);
            if (fabs(ip[1].S-X) < EPS)
              x = min(x, V / ip[1].F);
            cout << "Case #" << t << ": " << x << endl;
          } else {
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
          }
        } else {
          cout << "Case #" << t << ": " << max(x,y) << endl;
        }
      } else {
        if (fabs(ip[0].S-X) < EPS || fabs(ip[1].S-X) < EPS){
          double x = 1e15;
          if (fabs(ip[0].S-X) < EPS)
            x = min(x, V / ip[0].F);
          if (fabs(ip[1].S-X) < EPS)
            x = min(x, V / ip[1].F);
          cout << "Case #" << t << ": " << x << endl;
        } else {
          cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        }
      }
    }
  }
}
int main(){
  IOS;
  cout << fixed;
  cout << setprecision(15);
  int nT;
  cin >> nT;
  for (int _t=1; _t<=nT; _t++){
    input();
    solve(_t);
  }
  return 0;
}

