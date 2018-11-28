#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <queue>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
int best,total,complete;
int k,l,s;
string a,b;
void f(string x,int p, int c) {
  if (p==s) {
    complete++;
    total+=c;
    best=max(best,c);
  }
  else {
    for(int i=0;i<k;i++) {
      string t=x+a[i];
      if (t.size()>b.size())
        t=t.substr(1);
      f(t,p+1,c+(t==b));
    }
  }
}
int main() {
  int zzz;
  cin>>zzz;
  for(int zz=1;zz<=zzz;zz++) {
    double o=0;
    string gar;
    cin>>k>>l>>s;
    cin>>a;
    cin>>b;
    best=0;
    total=0;
    complete=0;
    f("",0,0);
    /*if (best==0)
      o=0;
    else*/
      o=(best*complete-1.0*total)/complete;
    printf("Case #%d: %.6f\n",zz,o);
  }
  return 0;
}
