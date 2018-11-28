#include <iostream>
#include <sstream>
#include <cstdlib>
using namespace std;
string int_to_string(int x) {
  stringstream ss;
  string s;
  ss<<x;
  ss>>s;
  return s;
}
bool match(string x,string y) {
  if (x.size()!=y.size()) {
      return false;
  }
  for (int i=0;i<x.size();i++) {
    if (y[i]!='?'&& x[i]!=y[i]) {
      return false;
    }
  }
  return true;
}
int main() {
  int cases;
  cin>>cases;
  for(int z=1;z<=cases;z++) {
    string bx,by,x,y;
    int best=9999;
    cin>>x>>y;
    for (int i=0;i<=999;i++) {
      string a=int_to_string(i);
      while(a.size()<x.size())a='0'+a;
      if (a.size()>x.size()) break;
      for (int j=0;j<=999;j++) {
        string b=int_to_string(j);
        while(b.size()<y.size())b='0'+b;
        if (b.size()>y.size()) break;
        if (match(a,x)&& match(b,y) && abs(i-j)<best) {
          best=abs(i-j);
          bx=a;
          by=b;
        }
      }
    }
    cout<<"Case #"<<z<<": "<<bx<<" "<<by<<endl;
  }
  return 0;
}
