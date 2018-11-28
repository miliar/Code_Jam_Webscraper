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
    set <ll> s;
    ll temp,n,p,k;
    freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	fast_IO
	cin>>k;
	rep(i,0,k)
	{
	    s.clear();
        cin>>n;
        ll temp=n;
        ll p=1;
        if (n==0)
        {
            cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
            continue;
        }
        while (s.size()<10)
        {
            while (temp!=0)
            {
                s.insert(temp%10);
                temp/=10;
            }
            ++p;
            temp=p*n;
        }
        cout<<"Case #"<<(i+1)<<": "<<temp-n<<endl;
	}
	return 0;
}
