#include <bits/stdc++.h>

#define ll long long
using namespace std;

int main(int argc, const char * argv[]){
int T;cin >> T;
for(int casen=0;casen<T;casen++){
ll X;cin >> X;
ll A=0;
ll seen=0;
ll ans=-1;
for(ll i=0;i<1000000;i++){
  A+=X;
  ll U=A;
  while(U){
    seen |=1<<(U%10);
    U/=10;
  };
  if(seen==(1<<10)-1){ans=A;break;}
}

  cout << "Case #"<<casen+1<<": ";
  if(ans!=-1)cout <<ans<<endl;
  else cout << "INSOMNIA"<<endl;
}
}
