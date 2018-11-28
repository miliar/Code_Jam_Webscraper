#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll>vll;
typedef pair<ll,ll> pll;
#define xx first
#define yy second
#define rep(n) for(i=0;i<n;i++)
#define pb push_back
#define mp make_pair
#define clr(a) memset(a, 0, sizeof a)
#define reset(a) memset(a, -1, sizeof a)
#define Clr(a) fill(a.begin(),a.end(),0)
#define Reset(a) fill(a.begin(),a.end(),-1)  
#define tr(c, it) \
  for(typeof(c.begin()) it=c.begin(); it!=c.end(); it++)  
  void debug(vector<ll> v)
{
    for(int i=0;i<v.size();i++)
        cout<<v[i]<<" ";
    cout<<"\n";
    // call debug({i,j,k})
}
ll m,n;
ll arr[11];
bitset<16>bits;
ll isprime(ll n)
{
	//cout<<n<<endl;
	for(ll i=2;i*i<=n;i++)
	{
		if(n%i==0)return i;
		//while(n%i==0)n/=i;
	}
	return -1;
}
void recur(ll ind)
{
	if(m==0)return;
	ll i,j;
	if(ind==n-1)
	{
		for(i=2;i<11;i++)
		{
			ll base=1;
			ll num=0;
			for(j=0;j<16;j++)
			{
				num+=bits[j]*base;
				base*=i;
				//cout<<bits[i]<<" ";
			}
			//cout<<num<<endl;
			arr[i]=isprime(num);
			 if(arr[i]==-1)
			 	return;
		}
		cout<<bits<<" ";
		for(i=2;i<11;i++)
			cout<<arr[i]<<" ";
		//cout<<bits.to_ullong();
		cout<<"\n";
		m--;
	}else 
	{
		bits[ind]=1;
		recur(ind+1);
		bits[ind]=0;
		recur(ind+1);
	}
}

int main()
{
    ll t,z,i,j,k,p,q,r,s,ans;
    scanf("%lld",&t);
    for(z=1;z<=t;z++)
    {
        scanf("%lld%lld",&n,&m);
        printf("Case #%lld:\n",z);
        bits[0]=bits[n-1]=1;
        //cout<<bits.to_ullong()<<endl;
        recur(1);
        //printf("%lld\n",ans);            
    }
    return 0;
} 