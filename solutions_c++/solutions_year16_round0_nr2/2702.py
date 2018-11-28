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
int arr[upperlimit+1];
int temp[upperlimit+1];
int main()
{
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);

    freopen("B-large.in","r",stdin);
    freopen("outlarge.txt","w",stdout);

	int t,i,j,k,n;
	string s;
	cin>>t;
	for(k=1;k<=t;k++){
		int answer=0;
		cin>>s;
		n=s.size();
		for(i=0;i<n;i++){
			if(s[i]=='+')arr[i]=1;
			else arr[i]=0;
		}
		if(s=="+")answer=0;
		else if(s=="-")answer=1;
		else{
            while(1){
                bool f=1;
                for(i=0;i<n;i++)if(arr[i]==0)f=0;
                if(f)break;
                if(arr[0]==0){
                    for(i=1;i<n;i++)if(arr[i]!=0)break;
                    for(j=0;j<i;j++)arr[j]=1-arr[j];
                }
                else{
                    for(i=1;i<n;i++)if(arr[i]==0)break;
                    for(j=0;j<i;j++)arr[j]=1-arr[j];
                }
                answer++;
            }
		}
		cout<<"Case #"<<k<<": "<<answer<<endl;
	}
	return 0;
}
