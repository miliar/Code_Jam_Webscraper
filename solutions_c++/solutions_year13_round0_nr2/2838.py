#include <iostream>
#include <fstream>
#define DN 105
using namespace std;

int T,n,m,target[DN][DN],init[DN][DN];

int main() {
  ifstream f("input.txt");
  ofstream g("output.txt");
  f>>T;
  for(int t=1; t<=T; ++t) {
    g<<"Case #"<<t<<": ";
    f>>n>>m;
    for(int i=0; i<n; ++i) for(int j=0; j<m; ++j) {
      init[i][j]=100;
      f>>target[i][j];
    }
    for(int i=0; i<n; ++i) {
      int hmax=0;
      for(int j=0; j<m; ++j) hmax=max(hmax,target[i][j]);
      for(int j=0; j<m; ++j) init[i][j]=min(init[i][j],hmax);
    }
    for(int j=0; j<m; ++j) {
      int hmax=0;
      for(int i=0; i<n; ++i) hmax=max(hmax,target[i][j]);
      for(int i=0; i<n; ++i) init[i][j]=min(init[i][j],hmax);
    }
    string rez="YES\n";
    for(int i=0; i<n; ++i) for(int j=0; j<m; ++j) if(init[i][j]!=target[i][j]) rez="NO\n";
    g<<rez;
  }
}
