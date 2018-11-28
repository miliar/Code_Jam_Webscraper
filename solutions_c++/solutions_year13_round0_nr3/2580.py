#include <iostream>
#include <fstream>
#include <vector>
#define Z7 10000000
#define LL long long
using namespace std;

vector<LL> nr;

int ispal(LL nr) {
  LL cnr=nr,rev=0;
  for(;cnr;rev=rev*10+cnr%10,cnr/=10);
  return rev==nr;
}

int main() {
  for(int i=1; i<=Z7; ++i) if(ispal(i) && ispal(i*1LL*i)) {
    nr.push_back(i*1LL*i);
    //cerr<<i<<' ';
  }
  //cout<<nr.size();cout.flush();
  int T,a,b;
  ifstream f("input.txt");
  ofstream g("output.txt");
  f>>T;
  for(int t=1; t<=T; ++t) {
    cerr<<t<<'\n';
    g<<"Case #"<<t<<": ";
    f>>a>>b;
    int r=0;
    for(int i=0; i<nr.size(); ++i) if(nr[i]>=a && nr[i]<=b) ++r;
    g<<r<<'\n';
  }
}
