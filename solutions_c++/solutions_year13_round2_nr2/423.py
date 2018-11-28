#include <fstream>
#include <string>
#include <iostream>
#include <cassert>
using namespace std;

ifstream in;
ofstream out;

int N,X,Y;

int f(int k) {
  return ((2*k+1)*(2*k+1)+2*k+1)/2;
}

double p(int k, int n) {
  if (k==0) return 1.0;
  if (n==0) return 0.0;
  return 0.5 * p(k,n-1) + 0.5 * p(k-1,n-1);
}

double solve() {
  cout<<"solve "<<N<<" "<<X<<" "<<Y<<endl;
  if (X<0) X=-X;
  int k = (X+Y)/2;
  int n0 = f(k-1); // minimo
  int n1 = f(k); // massimo
  cout<<"n0="<<n0<<" n1="<<n1<<" k="<<k<<endl;
  if (N>=n1) return 1.0; 
  if (N<=n0) return 0.0;
  if (X==0) return 0.0; // il vertice, mi serve N>=n1
  int n = N - n0;
  assert(Y>=0);
  assert(Y<2*k+1);
  if (n-2*k > Y) return 1.0; 
  // ho n lettere tra S e D
  // pb. che almeno Y+1 siano D.
  cout<<"kk="<<Y+1<<" n="<<n<<endl;
  return p(Y+1,n);
}

int main(int argc, char *argv[]) {
  assert(argc==3 || argc==4);
  string name=string(argv[1])+"-"+argv[2];
  if (argc==4)
    name += string("-")+argv[3];
  in.open((name+".in").c_str());
  assert(in);
  out.open((name+".out").c_str());
  assert(out);
  int T;
  in >> T;
  for (int t=1;t<=T;++t) {
    cout<<"t="<<t<<endl;
    in>>N>>X>>Y;
    out.precision(10);
    out.setf( std::ios::fixed, std:: ios::floatfield );
    out<<"Case #"<<t<<": "<<solve()<<endl;
  }
  return 0;
}
