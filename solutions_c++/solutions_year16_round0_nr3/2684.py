#include <bits/stdc++.h>
typedef long long ll;

using namespace std;



ll modulo(ll base, ll exponent, ll mod)
{
    ll x = 1;
    ll y = base;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            x = (x * y) % mod;
        y = (y * y) % mod;
        exponent = exponent / 2;
    }
    return x % mod;
}
 
/* 
 * Fermat's test for checking primality 
 */
bool Fermat(ll p, int iterations)
{
    if (p == 1)
    {
        return false;
    }
    for (int i = 0; i < iterations; i++)
    {
        ll a = rand() % (p - 1) + 1; 
        if (modulo(a, p - 1, p) != 1)
        { 
            return false;
        }
    }
    return true;
}


int main() {
  ios_base::sync_with_stdio(false);
  ll np=1e8;
  ll m=sqrt(np)+1;
  vector<bool> v(np,true);
  vector<ll> primes;
  for (ll i=2; i<m;i++){
    if (!v[i]) continue;
    primes.push_back(i);
    for (ll j = i+i; j<np; j+= i) 
      v[j]=false;
  }
  int t,n,j;
  cin >> t;
  cin >> n >> j;  
  cout << "Case #"<<1<<":\n";
  ll base =(1<<(n-1))+1;
  ll top=1<<(n-2);
  int cases=0;
  for (ll k =0; k< top; k++) {
    ll num=base + (k<<1);
    bool jamcoin = true;
    vector<ll> div(11);
    bitset<33> x(num);
    for (int b=2; b<11; b++) {
      ll st=1,nb=0;
      for (int i=0; i <n; i++){
	if (x[i]) 
	  nb += st;
	st *= b;
	
      }
      if (Fermat(nb,70)) {
	jamcoin=false; 
	break;
      }
      ll co=0;
      while ((co<(int)primes.size()) and (nb%primes[co]!=0)) 
	co++;
      if (co==(int)primes.size()) {jamcoin=false;break;}
      div[b]=primes[co];
      }
    if(jamcoin) {
      for (int i=n-1; i>=0; i--)
	cout  << x[i];
      cout <<" ";
      for (int i=2; i<11; i++) 
	cout << div[i]<<" ";
      cout <<endl;
      cases++;
    }
    if (cases==j) return 0;  
  } 
}
