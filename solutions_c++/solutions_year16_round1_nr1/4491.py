#include <bits/stdc++.h>
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

set <string> set1;
set <string> :: iterator it;
vecs v;

void go(string formed,string s, ll pos)
{
    if (pos>=s.length())
        return;
    else if (pos==s.length()-1)
    {
        set1.insert(formed+s[pos]);
        set1.insert(s[pos]+formed);
        return;
    }
    else
    {
        go(formed+s[pos],s,pos+1);
        go(s[pos]+formed,s,pos+1);
    }
}


int main()
{
    freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	fast_IO
	ll t;
	cin>>t;
	rep(i,1,t+1)
	{
	    set1.clear();
	    v.clear();
        string s="";
        cin>>s;
        go("",s,0);
        for(it=set1.begin();it!=set1.end();it++)
            v.pb(*it);
        cout<<"Case #"<<i<<": "<<v[v.size()-1]<<endl;
	}
	return 0;
}
