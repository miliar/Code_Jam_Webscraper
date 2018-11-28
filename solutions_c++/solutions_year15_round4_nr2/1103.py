#include<bits/stdc++.h>
using namespace std;

typedef pair<double,double> P;
int T,N;
double X,C;
vector<P> R;
const double EPS = 1E-10;

bool eq(double a,double b){
  return abs(a-b) < EPS;
}

int main(){
  cin >> T;
  for(int ttt=0;ttt<T;ttt++){
    cin >> N >> X >> C;
    R.clear();
    for(int i=0;i<N;i++){
      double a,b; cin >> a >> b;
      R.push_back(P(a,b));
    }

    double res = -1.0;
    if( N == 1 ){
      if( eq( R[0].second, C ) ) {
        res = X / R[0].first;
      } 
    } else if( N == 2 ){
      if( eq( R[1].second, R[0].second ) ){
        if( eq(C , R[0].second) ){
          double st = 0.0, ed = min( X/R[0].first, X/R[1].first);
          while( !eq(st,ed) ){
            double h = (st + ed)/2.0;
            if( R[0].first * h + R[1].first * h < X ){
              st = h;
            } else {
              ed = h;
            }
          }
          res = ed;
        }
      } else {
        double v1 = ( C - R[0].second ) * X / ( R[1].second - R[0].second );
        double v0 = X - v1;
        //        cout << v1 << " "<< v0 << endl;
        //cout << ( v0 * R[0].second + v1 * R[1].second ) / X << endl; 
        if( v1 > -EPS && v0 > -EPS ){
          res = max(v0/R[0].first, v1/R[1].first);
        }
      }
    }
    //  cout << N << " " <<X << " "<< C <<endl;
    cout << "Case #" << ttt+1 << ": ";
    if( res < -EPS ) cout << "IMPOSSIBLE" << endl;
    else printf("%.10lf\n",res);
  }
}
