#include <bits/stdc++.h>

using namespace std;

void solve() {
  long long n; cin>>n;
  if(n == 0) {
    cout<<"INSOMNIA"<<endl;
    return;
  }
  int cm = 0;
  long long cc = n;
  for(;;cc+=n) {
    long long tmp = cc;
    while(tmp > 0) {
      cm|=(1<<(tmp % 10));
      tmp/=10;
    }
    if(cm == 1023) break;
  }
  cout<<cc<<endl;

}

int main() {
  assert(freopen("input.txt","r",stdin));
  assert(freopen("output.txt","w",stdout));
  int t; cin>>t;
  for(int i = 1;i <= t;i++) {
    cerr<<"Executing Case #"<<i<<endl;
    cout<<"Case #"<<i<<": ";
    solve();
  }

}
