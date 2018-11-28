#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int check(ll n){
  int bit=0;
  while(n){
    bit|=(1<<(n%10));
    n/=10;
  }
  return bit;
}

int main(){

  int Q;
  cin>>Q;
  for(int q=0;q<Q;q++) {
    cout <<"Case #"<<q+1<<": ";
    ll n,bit=0;
    cin>>n;
    
    ll sum=n;
    while(n&&bit!=(1<<10)-1){
      bit|=check(sum);
      sum+=n;
    }
    if(sum) cout << sum-n<<endl;
    else cout <<"INSOMNIA"<<endl;
  }

  return 0;
}
