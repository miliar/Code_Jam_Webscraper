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
lld change(lld n, lld b) {
	lld res = 0, mult=1;
	while (n > 0) {
		res += mult*(n%10);
		mult *= b;
		n/=10;
	}
	return res;
}

lld div (lld n) {
	for (lld i = 2; i*i <= n; i++)
		if (n%i == 0)
			return i;
	return 1;
}
lld base2(lld i) {
	lld res = 0, mult = 1;
	while (i > 0) {
		if (i%2)
			res += mult;
		mult*=10;
		i/=2;
	}
	return res;
}
int main()
{
  ios_base::sync_with_stdio(false);
  cout.precision(10);
  cout << fixed;
  int t;
  cin>>t;
  int T=t;
  while (t--) {
	  int n,j;
	  cin>>n>>j;
	  int created = 0;
	  cout<<"Case #"<<T-t<<":\n";
	  for (lld i = 0; i < (1<<n-2); i++) {
		  lld nu = pow(10, n-1)+1+base2(i)*10;
		  vector<lld> proof;
		  for (int base = 2; base <= 10; base++) {
			  lld d = div(change(nu, base));
			  if (d != 1)
				  proof.pb(d);
		  }
		  if (created >= j)
			  break;
		  if (proof.sz == 9) {
			  created++;
			  cout<<nu<<" ";
			  for (int k = 0; k < proof.sz - 1; k++)
				  cout<<proof[k]<<" ";
			  cout<<proof[proof.sz-1]<<"\n";
		  }
	  }
  }

  if(debug)cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
	return 0;
}
