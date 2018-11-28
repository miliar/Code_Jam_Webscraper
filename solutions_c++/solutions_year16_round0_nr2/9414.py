#include <bits/stdc++.h>
using namespace std;
struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0); cin.tie(0);cout.tie(0); } } _;

template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
vector<long long int>prime;void sieve(long long int MAX){bool status[MAX+7];for(int i=2; i<=MAX; i++)status[i]=true;for(int i=4; i<=MAX; i+=2)status[i]=false;int sqrtn=sqrt(MAX);for(int i=3; i<=sqrtn; i+=2)if(status[i])for(int j=i*i; j<=MAX; j+=(i+i))status[j]=false;for(int i=2; i<=MAX; i++)if(status[i])prime.push_back(i);}
bool isprime(long long int n){if(n==1)return false;long long int i;if(n==2)return true;if(n%2==0)return false;for(i=3;i<=sqrt(n);i+=2)if (n%i==0)return false;return true;}

#define READ(FILE) freopen(FILE,"r",stdin)
#define WRITE(FILE) freopen(FILE,"w",stdout)

#define ict int t;cin>>t;while(t--)
#define lct long long int t;cin>>t;while(t--)
#define in(a) int a; cin>>a;
#define llin(a) ll a; cin>>a;

#define srep(i,a,b) for(ll i=a;i<b;i++)
#define rep(i,n) for(ll i=0;i<n;i++)

#define pb push_back
template <typename T> std::string to_str(T value) {std::ostringstream os;os << value ;return os.str();}
typedef long long int ll; // [9,223,372,036,854,775,807 to -9.....808]
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<ll,ll> pll;
typedef set<int> si;
typedef set<ll> sl;
typedef map<string, ll> mapsl;
typedef map<string, int> mapsi;
typedef map<int,int> mapii;
typedef map<ll, ll> mapll;
int main()
{
    READ("B-large.in");
    WRITE("output.txt");
	llin(t);
	for(ll j=1;j<=t;j++)
	{
        string str;
		cin>>str;
		ll cnt=0;
		ll len = str.length();
		while(1)
		{
			ll i=0;
			if(str[i]=='+')
			{
				while(str[i]=='+' && i<len)
					i++;
				if(i!=len)
				{
				    for(ll g=0;g<i+1;g++)
                        str[g]='-';
					cnt+=1;
				}
				else
				{
					break;
				}
			}
			else if(str[i]=='-')
			{
				while(str[i]=='-' && i<len)
					i++;
				if(len!=i)
				{
				    for(ll g=0;g<i+1;g++)
                        str[g]='+';
					cnt+=1;
				}
				else
				{
					cnt+=1;
					break;
				}
			}
		}
		cout<<"Case #"<<j<<": "<<cnt<<endl;
	}
}
