#include <bits/stdc++.h>
using namespace std;

int a[10005];      

int main() {
  int t;
  cin>>t;
  for(int z=1; z<=t; z++) {
    cout<<"Case #"<<z<<": ";
    int n;
    cin>>n;
    for(int i=0; i<n; i++) {
      cin>>a[i];
      assert(a[i]<=1000);
    }
    int res = 1e9;
    for(int j=1; j<=1000; j++) {
      int cur = 0;
      for(int i=0; i<n; i++) {
        int x = a[i];
        while(x>j) {
          x-=j;
          cur++;
        }
      }
      res = min(res,cur+j);
    }
    cout<<res<<endl;
  }
        
  return 0;
}
