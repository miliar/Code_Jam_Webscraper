#include <bits/stdc++.h>
typedef long long ll;

using namespace std;


int gcd(int gran, int petit) 
{
  if (petit==0) 
    return gran;
  else
    return gcd(petit,gran%petit);
}

int main() {
  ios_base::sync_with_stdio(false);
  ll t,n;
  cin >> t;
  vector<ll> a(t,-1);
  for (ll i=0; i< t; i++) {
    cin >> n;
    vector<bool> d(10,false);
    ll lim=100*n*n;
    for (ll j=1; j<=lim; j++) {
      ll m=n*j;
      while (m>0) {
	d[m%10]=true;
	m=m/10;
      }
     bool sleep=true;
     for (int k=0; k<10; k++) 
       if (!d[k]) sleep=false;
     if (sleep) {a[i]=j*n; break;}
    }     
  }
  for (ll i=0; i< t; i++) {
    cout << "Case #"<<i+1<<": ";
    if (a[i]==-1) 
      cout<< "INSOMNIA\n";
    else
      cout<< a[i]<<"\n";
  }
  return 0;
}
