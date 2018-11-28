#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;
int f(int x,vector<int> v) {
  int c=0;
  for(int i=0;i<v.size();i++)
    if (v[i]>=x)
      c+=v[i]/x-1+(v[i]%x>0);
  return x+c;
}
int main() {
  int zzz;
  cin>>zzz;
  for(int zz=1;zz<=zzz;zz++) {
    int n;
    int best=1000;
    cin>>n;
    vector<int> v;
    v.clear();
    for(int i=0;i<n;i++) {
      int x;
      cin>>x;
      v.push_back(x);
    }
    for(int i=1;i<=2000;i++) {
      best=min(best,f(i,v));
    }
    printf("Case #%d: %d\n",zz,best);
  }
  return 0;
}
