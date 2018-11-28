#include<bits/stdc++.h>
#include<limits.h>
using namespace std;

#define mod 1000000007
#define si(x) scanf("%d", &x)
#define sll(x) scanf("%lld", &x)
#define pi(x) printf("%d\n", x)
#define pll(x) printf("%lld\n", x)
#define ii pair<int, int>
#define vi vector<int>
#define vii vector<pair<int, int> >
#define adjList vector<vector<int> >
#define ll long long int
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define rep(i, z, q) for(i = z; i < q; i++)
#define rev(i, z, q) for(i = z; i > q; i--)

ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }
ll power(ll a,ll b) {
  ll ans = 1;  
  while(b > 0){
    if(b & 1)
      ans = ((ans % mod) *(a % mod)) % mod;
    a=((a % mod)*(a % mod)) % mod;
    b >>= 1;
  }
  return ans;
}

int main() {

  int t, i, n, p[10000], ind = 1;

  cin>>t;
  
  while(t--) {
    cin>>n;
    pair<int, char> p[n+1];
    
    rep(i, 0, n) { 
      cin>>p[i].fi;
      p[i].se = i + 'A';
    }

    sort(p, p+n);

    cout<<"Case #"<<ind<<": ";
    
    while(p[n-1].fi != p[n-2].fi) {
      if(p[n-1].fi - 2 >= p[n-2].fi) {
	cout<<p[n-1].se<<p[n-1].se<<" ";
	p[n-1].fi -= 2;
      }
      else {
	cout<<p[n-1].se<<" ";
	p[n-1].fi -= 1;
      }
    }
    
    rep(i, 0, n-2) {
      while(p[i].fi != 0) {
	cout<<p[i].se<<" ";
	p[i].fi--;
      }
    }
    
    while(p[n-2].fi != 0) {
      cout<<p[n-1].se<<p[n-2].se<<" ";
      p[n-2].fi--;
    }
    cout<<endl;
    ind++;
  }
  
  return 0;
}

