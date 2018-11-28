//Rupinder

#include<bits/stdc++.h>
#define debug 0
#define lld long long
#define FOR(i,a,b) for(i= a ; i <= b ; ++i)
#define rep(i,n) for(i= 0 ; i < n ; ++i)
#define repn(i,n) FOR(i,1,n)
#define all(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
#define pb push_back
#define sz size()
#define pii pair<int, int>
#define pll pair <lld ,lld>
#define mp make_pair
#define fill(x,v) memset(x,v,sizeof(x))
#define scan(v,n) vector<int> v(n);rep(i,n)cin>>v[i];
#define vi vector<int>
#define MOD 1000000007
#define ff first
#define ss second

using namespace std;
lld modpow(lld a,lld n,lld temp){lld res=1;while(n>0){if(n&1)res=(res*a)%temp;a=(a*a)%temp;n>>=1;}return res%temp;} 

int main()
{
  ios_base::sync_with_stdio(false);
  cout.precision(10);
  cout << fixed;
  int t;
  cin>>t;
  int T=t;
  while (t--) {
	  string s;
	  cin>>s;
	  int seg = 0, first = 0;
	  if (s[0] == '-') first++;
	  for (int i = 1; i < s.sz; i++)
		  if (s[i] == '-' && s[i-1] != '-')
			  seg++;
	  cout<<"Case #"<<T-t<<": "<<first + 2*seg<<"\n";
  }


  if(debug)cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
	return 0;
}
