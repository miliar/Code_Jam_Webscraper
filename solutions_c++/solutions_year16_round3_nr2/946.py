#include <iostream>
using namespace std;
int main() {
  int cases;
  cin>>cases;
  for(int z=1;z<=cases;z++) {
    long long n,k;
    cin>>n>>k;
    if ((1<<(n-2))>=k) {
      cout<<"Case #"<<z<<": POSSIBLE"<<endl;
      k--;
      for (int i=1;i<=(n-1);i++) {
        for (int j=1;j<=(n-1);j++) {
          if (j>i) {
            cout<<1;
          } else {
            cout<<0;
          }
        }
        if (i==1) {
          cout<<1;
        } else {
          if (k%2==1) {
            cout<<1;
          } else {
            cout<<0;
          }
          k/=2;
        }
        cout<<endl;
      }
      for (int i=1;i<=n;i++) {
        cout<<"0";
      }
      cout<<endl;
    } else {
      cout<<"Case #"<<z<<": IMPOSSIBLE"<<endl;
    }
  }
  return 0;
}
