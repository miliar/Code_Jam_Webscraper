#include <iostream>
#include <fstream>
#define DN 1005
using namespace std;

int t,n,v[DN];

int main() {
  ifstream f("input.txt");
  ofstream g("output.txt");
  f>>t;
  for(int T=1; T<=t; ++T) {
    f>>n;
    int hm=0;
    for(int i=0; i<n; ++i) {
      f>>v[i];
      hm=max(hm,v[i]);
    }
    int r=(1<<30);
    for(int i=1; i<=hm; ++i) {
      int rc=0;
      for(int j=0; j<n; ++j) rc+=((v[j]-1)/i);
      //cout<<i<<' '<<rc<<'\n';
      r=min(r,rc+i);
    }
    
    g<<"Case #"<<T<<": "<<r<<'\n';
  }
}