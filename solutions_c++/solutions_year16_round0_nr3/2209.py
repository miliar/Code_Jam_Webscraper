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
		if(exponent&1)ans=(ans*base);
		base=(base*base);
		exponent/=2;
	}
	return ans;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    freopen("C-large.in","r",stdin);
    freopen("outlargeC.txt","w",stdout);

	int t,n,cnt,i,j,k;
	cin>>t;
	while(t--){
        cout<<"Case #1: "<<endl;
        cin>>n>>cnt;
        int temp=(n-4)/2;
        for(i=1;i<=cnt;i++){
            string s="1";
            int temp1=i;
            for(k=0;k<temp;k++){
                if(temp1%2==0)s+="0";
                else s+="1";
                temp1/=2;
            }
            s+="1";
            s+=s;
            cout<<s;
            for(j=2;j<=10;j++)cout<<" "<<(1+powmod(j,2+temp));
            cout<<endl;
        }
	}

	return 0;
}
