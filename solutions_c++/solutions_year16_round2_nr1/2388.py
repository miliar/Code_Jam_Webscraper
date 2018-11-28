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

int main()
{
    freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	fast_IO
	ll n;
	cin>>n;
	rep(i,1,n+1)
	{
	ll a[10]={0};
	map <char,ll> m;
	    string s;
	    cin>>s;
	    rep(i,0,s.length())
	    {
	        if (m.find(s[i])==m.end())
	        m[s[i]]=(1);
	        else
                m[s[i]]++;
	    }
        cout<<"Case #"<<i<<": ";
        //map <char,ll>:: iterator it;
	    if (m.find('Z')!=m.end())
        {
            while (m['Z']!=0)
            {
                m['Z']--;
                m['E']--;
                m['R']--;
                m['O']--;
                a[0]++;
            }
        }
        if (m.find('W')!=m.end())
        {
            while (m['W']!=0)
            {
                m['T']--;
                m['W']--;
                m['O']--;
                a[2]++;
            }

        }
        if (m.find('X')!=m.end())
        {
            while (m['X']!=0)
            {
                m['S']--;
                m['I']--;
                m['X']--;
                a[6]++;
            }
        }
        if (m.find('G')!=m.end())
        {
            while (m['G']!=0)
            {
                m['E']--;
                m['I']--;
                m['G']--;
                m['H']--;
                m['T']--;
                a[8]++;
            }
        }
        if (m.find('H')!=m.end())
        {
            while (m['H']!=0)
            {
                m['T']--;
                m['H']--;
                m['R']--;
                m['E']--;
                m['E']--;
                a[3]++;
            }
        }
        if (m.find('U')!=m.end())
        {
            while (m['U']!=0)
            {
                m['F']--;
                m['O']--;
                m['U']--;
                m['R']--;
                a[4]++;
            }
        }
        if (m.find('F')!=m.end())
        {
            while (m['F']!=0)
            {
                m['F']--;
                m['I']--;
                m['V']--;
                m['E']--;
                a[5]++;
            }
        }
        if (m.find('V')!=m.end())
        {
            while (m['V']!=0)
            {
                m['S']--;
                m['E']--;
                m['V']--;
                m['E']--;
                m['N']--;
                a[7]++;
            }
        }
        if (m.find('O')!=m.end())
        {
            while (m['O']!=0)
            {
                m['O']--;
                m['N']--;
                m['E']--;
                a[1]++;
            }
        }
        if (m.find('E')!=m.end())
        {
            while (m['E']!=0)
            {
                m['E']--;
                m['I']--;
                m['N']--;
                m['N']--;
                a[9]++;
            }
        }
        rep(i,0,10)
            {
                while (a[i]>0)
                {
                    cout<<i;
                a[i]--;
                }
            }
        cout<<endl;
	}

	return 0;
}
