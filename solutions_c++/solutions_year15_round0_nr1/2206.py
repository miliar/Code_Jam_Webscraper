#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
  int t;
  cin>>t;
  for(int z=1; z<=t; z++) {
    cout<<"Case #"<<z<<": ";
    int n;
    cin>>n;
    string s;
    cin>>s;
    vector<int> a(n+1), b(n+1);
    for(int i=0; i<=n; i++) {
      a[i] = s[i]-'0';
    }
    int lo = 0, hi = 100000;
    while(lo<hi) {
      int mi = (lo+hi)/2;
      b[0] = a[0]+mi;
      bool f = true;
      for(int i=1; i<=n; i++) {
        if(b[i-1]<i) {
          f = false;
          break;
        }
        b[i] = b[i-1]+a[i];
      }
      if(f) hi = mi;
      else lo = mi+1;
    }
    cout<<hi<<endl;
  }
        
  return 0;
}
