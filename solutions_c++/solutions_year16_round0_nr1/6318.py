#include <iostream>
#include <stdlib.h>
#define ll unsigned long long int
using namespace std;

bool check(ll v[]) {
  bool r = true;
  for (int i = 0; i < 10; i++) {
    //cout<<v[i]<<" ";
    if (!v[i])
      r = false;
  }
  //cout<<endl;
  return r;
}

void set(ll num,ll  v[]) {
  while(num) {
    v[num%10] = 1;
    num /= 10;
  }
}

int main() {
  ll T, N;
  ll v[10];
  cin>>T;

  for (int k = 0; k < T; k++) {
    cin>>N;
    ll ans = -1;
    if (N != 0){    
      
      memset(v, 0, sizeof(v));

      ll num = N;
      ll i = 1;
      while(!check(v)) {
        num = N * i;
        i++;
        set(num, v);
      }
      ans = num;
    }

    cout<<"Case #"<<(k+1)<<": " ;
    if (ans == -1)
      cout<<"INSOMNIA"<<endl;
    else
      cout<<ans<<endl;
  }
}