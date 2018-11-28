#include<bits/stdc++.h>
#include<limits.h>
using namespace std;

#define mi 1000000007

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
      ans = ((ans % mi) *(a % mi)) % mi;
    a=((a % mi)*(a % mi)) % mi;
    b >>= 1;
  }
  
  return ans;
}

bool flag[11];

int main() {
  int n, t, i, ind = 1;

  cin>>t;
  
  while(t--) {
    cin>>n;

    if(n == 0)
      cout<<"Case #"<<ind<<": INSOMNIA"<<endl;

    else {
      
      rep(i, 0, 10)
	flag[i] = false;
      
      int temp, j = 1, count = 10;
    
      while(1) {
	
	temp = n * j;
	
	while(temp > 0) {
	  if(flag[temp%10] == false) {
	    flag[temp%10] = true;
	    count--;
	  }
	  
	  temp /= 10;
	  
	  if(count == 0)
	    break;
	}
	
	if(count == 0)
	  break;
	j++;
      }
      cout<<"Case #"<<ind<<": "<<n*j<<endl;
      
    }
    ind++;
  }
  
  return 0;
}

