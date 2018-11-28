#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;

typedef long long ll;

ll ipower(ll a, ll b){
  if(b == 0) return 1;
  if(b%2 == 0) return ipower(a, b/2)*ipower(a, b/2);
  else return ipower(a, (b-1)/2)*ipower(a, (b-1)/2)*a;
}

ll convert(ll jc, ll base){
  ll d=0, n, res=0;
  n = jc;
  do{
    res += (n%10)*ipower(base, d);
    n /= 10;
    d++;
  }while(n != 0);
  return res;
}

ll binary(ll jc){
  ll d=0, n, res=0;
  n = jc;
  do{
    res += (n%2)*ipower(10, d);
    n /= 2;
    d++;
  }while(n != 0);
  return res;
}

ll divisor(ll n){
  if(n == 2) return -1;

  if(n%2 == 0)
    return 2;

  ll i = 3;
  while(i <= (ll) sqrt(n)){
    if(n%i == 0) return i;
    i += 2;
  }

 return -1;
}

int main(void){
  ll T, N, J, max, di, count=0;
  ll stock[11];
  bool flag;

  cin >> T;
  cin >> N >> J;

  max = ipower(2, N-2)-1;

  for(ll i=1;i<=T;i++){
    cout << "Case #" << i << ":" << endl;
    for(ll j=0;j<=max;j++){
      flag = true;
      ll jamcoin = ipower(10, N-1)+binary(j)*10+1;

      for(int k=2;k<=10 && flag == true;k++){
        di = divisor(convert(jamcoin, k));
        if(di != -1) stock[k] = di;
        else flag = false;
      }

      if(flag){
        count++;
        cout << jamcoin << " ";
        for(int k=2;k<10;k++) cout << stock[k] << " ";
        cout << stock[10] << endl;
      }
      if(count == J) break;
    }
  }

  return 0;
}
