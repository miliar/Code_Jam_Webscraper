#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front
#define vi vector<int>
#define vl vector<ll>
#define vii vector<pii >
#define vll vector<pll>
#define pll pair<ll,ll>
#define pii pair<int,int>
#define pi 3.14159265358979
#define EL printf("\n")
#define OK printf("OK");
#define foreach(i,t) for(auto i =t.begin();i!=t.end();i++) 
#define pii pair<int,int>
#define pdn(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%d",&n)
#define pn printf("\n")
#define  omap unordered_map
#define PI 3.14159265
#define Inf 1e9
#define mod 1000000007
#define precise(n,k) fixed<<setprecision(k)<<n
#define fequal(a,b) (fabs(a - b)<(1e-9))
typedef long long ll;
typedef long double lf;

ll gcd(ll a,ll b){return (b==0)? a:gcd(b,a%b); }
void nope(int dec = 0){if(!dec) cout<<"NO";else cout<<"YES";exit(0);}

char invert(char a)
{
	if(a=='+')
		return '-';
	else
		return '+';
}
int main()
{
	std::ios::sync_with_stdio(false);cin.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		bool ans=true;
		ll val=0;
		int len=s.length();
		for(int i=0;i<len;i++)
		{
			if(s[i]=='-')
			{
				if(i+k-1>=len)
				{ans=false; break;}

				for(int j=i;j<=i+k-1;j++)
					s[j]=invert(s[j]);
				val++;
			}
		}
		cout<<"Case #"<<p<<": ";
		if(ans)
			cout<<val<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}