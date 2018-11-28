#include <bits/stdc++.h>
#include <string>
#define pb push_back
#define mp make_pair
#define s(a) sort(a.begin(),a.end())
#define vecll vector<long long int>
#define vecs vector<string>
#define vecpll vector<pair<long long int,long long int> >
#define rep(i,a,b) for(long long int (i)=(a);(i)<(b);(i)++)
#define repr(i,b,a) for(long long int (i)=(b);(i)>=(a);(i)--)
#define fast_IO ios_base::sync_with_stdio(false);cin.tie(0);
#define while_tc long long int t;cin>>t;while(t--)
#define ispow2(n) (n&&(!(n&(n-1))))      ///check if its perfect power of 2
#define MOD 1000000007
typedef long long int ll;
using namespace std;
template <typename T>
T modpow(T base, T exp) {
  /// base %= modulus;
  T result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base); ///  % modulus;
    base = (base * base); ///  % modulus;
    exp >>= 1;
  }
  return result;
}


int main()
{
    freopen("B-large.in","r",stdin);
	freopen("output1.txt","w",stdout);
	fast_IO
	ll k;
	cin>>k;
	rep(i,0,k)
	{
	    string s="";
	    cin>>s;
	    ll ans=0;
	    ll l=s.length()-1;
	    while (l>-1)
        {
            while (l>=0 && s[l]=='+')
                l-=1;
            if (l==-1)
                break;
            rep(i,0,l+1)
            {
                if (s[i]=='-')
                    s[i]='+';
                else
                    s[i]='-';
            }
            l-=1;
            ans+=1;
        }
        cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}
	return 0;
}
