#include <vector>
#include <string>
#include <iostream>
#include <queue>
#include <map>
#include <math.h>
using namespace std;

int DEBUG=0;

double doit(int N, double V, double X, vector<double> v, vector<double> w) {
  if(v.size()==1) {
    if(fabs(w[0]-X)>1e-9) return -1;
    return V/v[0];
  }
  if(fabs(w[0]-w[1])<1e-9) {
    if(fabs(w[0]-X)>1e-9) return -1;
    return V/(v[0]+v[1]);
  }
  if(w[0]>w[1]) {
    swap(w[0],w[1]);
    swap(v[0],v[1]);
  }
  double lo=0,hi=1;
  for(int i=0;i<1000;i++) {
    double mid=(lo+hi)/2;
    double V1=V*mid,V2=V*(1.0-mid);
    double T=(V1*w[0]+V2*w[1])/(V1+V2);
    if(T<X) hi=mid;
    else lo=mid;
  }
  double V1=V*lo,V2=V*(1.0-lo);
  double T=(V1*w[0]+V2*w[1])/(V1+V2);
  if(fabs(T-X)>1e-9) return -1;
  return max(V1/v[0],V2/v[1]);
}

int main() {
  int tests;
  cin >> tests;
  for(int i = 0; i < tests; i++) {    
    int N; double V,X;
    cin>>N>>V>>X;
    vector<double> v,w;
    for(int j=0;j<N;j++) {
      double R,C;
      cin>>R>>C;
      v.push_back(R);
      w.push_back(C);
    }
    double val=doit(N,V,X,v,w);
    if(val<0) { cout << "Case #" << (i+1) << ": IMPOSSIBLE"<<endl; continue; }
    cout << "Case #" << (i+1) << ": ";
    std::cout.precision(30);
    cout << doit(N,V,X,v,w) << endl;
  }
  return 0;
}
