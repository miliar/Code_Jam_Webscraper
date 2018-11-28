#include <iostream>
#include <fstream>
#include <string>
#define DN 1005
#define LL long long
using namespace std;

string inp;
int T,n,J;
LL nr[12];

int isp(LL k) {
  for(LL i=2; i*i<=k; ++i) if(k%i==0) return 0;
  return 1;
}

LL fdiv(LL k) {
  for(LL i=2; i*i<=k; ++i) if(k%i==0) return i;
  return -1;
}

int main() {
  ifstream f("input.txt");
  ofstream g("output.txt");
  f>>T;
  for(int t=1; t<=T; ++t) {
    f>>n>>J;
    g<<"Case #"<<t<<": \n";
    int cr=0;
    //vector<int> nr;
    for(LL nc=(1LL<<(n-1)); nc<(1LL<<n) && cr<J; ++nc) if(nc&1) {
      LL pb[12];
      for(int k=2; k<=10; ++k) {
        pb[k]=1;
        nr[k]=0;
      }
      //for(int i=n-1; i>=0; --i) cout<<((nc&(1<<i))!=0);
      //cout<<'\n';
      for(int j=0; j<n; ++j) {
        if(nc&(1LL<<j)) {
          for(int k=2; k<=10; ++k) {
            nr[k]+=pb[k];
            //cout<<nc<<' '<<k<<' '<<j<<' '<<nr[k]<<' '<<pb[k]<<'\n';
          }
        }
        for(int k=2; k<=10; ++k) pb[k]*=k;
      }

      int ok=1;
      //for(int i=n-1; i>=0; --i) cout<<((nc&(1<<i))!=0);
      //cout<<'\n';
      //cout<<nr[2]<<' '<<nr[3]<<' '<<nr[4]<<'\n';
      for(int k=2; k<=10; ++k) if(isp(nr[k])) ok=0;
      if(ok) {
        ++cr;
        for(int i=n-1; i>=0; --i) g<<((nc&(1LL<<i))!=0);
        g<<' ';
        for(int k=2; k<=10; ++k) g<<fdiv(nr[k])<<' ';
        g<<'\n';
      }
    }
  }
}