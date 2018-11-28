#include <bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define upperlimit 1000100
#define INF 1e18
#define eps 1e-8
#define endl '\n'
#define mp make_pair
#define pb push_back
#define pcc pair<char,char>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define F first
#define S second

using namespace std;

ll gcd(ll n1,ll n2){
	if(n1%n2==0)return n2;
	return gcd(n2,n1%n2);
}
ll powmod(ll base,ll exponent)
{
	ll ans=1;
	while(exponent){
		if(exponent&1)ans=(ans*base)%mod;
		base=(base*base)%mod;
		exponent/=2;
	}
	return ans;
}
bool dig[10];
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    freopen("A-large.in","r",stdin);
    freopen("outlargeA.txt","w",stdout);

	int t,n,i,j,k;
	cin>>t;
	for(k=1;k<=t;k++){
		cin>>n;
		if(n==0)cout<<"Case #"<<k<<": INSOMNIA\n";
		else{
			int temp=0;
			for(i=0;i<10;i++)dig[i]=0;
			while(1){
				bool f=1;
				for(i=0;i<10;i++)if(dig[i]==0)f=0;
				if(f)break;
				temp+=n;
				int temp1=temp;
				while(temp1){
					dig[temp1%10]=1;
					temp1/=10;
				}
			}
			cout<<"Case #"<<k<<": "<<temp<<endl;
		}
	}

	return 0;
}
