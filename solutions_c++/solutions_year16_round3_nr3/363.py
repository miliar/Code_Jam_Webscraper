#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
int a,b,c,l;
struct outfit {
  int a,b,c;
};
vector<outfit> v;
vector<outfit> best;
bool used[1100];
int ab[11][11],bc[11][11],ac[11][11];
void f(int p,int t) {
  if (p==v.size()) {
    if (t>best.size()) {
      memset(ab,0,sizeof(ab));
      memset(ac,0,sizeof(ac));
      memset(bc,0,sizeof(bc));
      for (int i=0;i<v.size();i++) {
        if (used[i]) {
          ab[v[i].a][v[i].b]++;
          ac[v[i].a][v[i].c]++;
          bc[v[i].b][v[i].c]++;
          if (ab[v[i].a][v[i].b]>l || ac[v[i].a][v[i].c]>l || bc[v[i].b][v[i].c]>l) {
            return;
          }
        }
      }
      best.clear();
      for (int i=0;i<v.size();i++) {
        if (used[i]) {
          best.push_back(v[i]);
        }
      }
    }
  } else {
    used[p]=true;
    f(p+1,t+1);
    used[p]=false;
    f(p+1,t);
  }
}
int main() {
  int cases;
  cin>>cases;
  for(int z=1;z<=cases;z++) {
    cin>>a>>b>>c>>l;
    outfit o;
    v.clear();
    memset(used,0,sizeof(used));
    for (int i=1;i<=a;i++) {
      for (int j=1;j<=b;j++) {
        for (int k=1;k<=c;k++) {
          o.a=i;
          o.b=j;
          o.c=k;
          v.push_back(o);
        }
      }
    }
    best.clear();
    f(0,0);
    cout<<"Case #"<<z<<": "<<best.size()<<endl;
    for (int i=0;i<best.size();i++) {
      cout<<best[i].a<<" "<<best[i].b<<" "<<best[i].c<<endl;
    }
  }
  return 0;
}
