#include<bits/stdc++.h>

#define pb(x) push_back(x);
#define gc getchar_unlocked
#define pc(x) putchar_unlocked(x);
#define inf 1<<30
#define ll long long   
#define mod 1000000007

using namespace std;

typedef pair<int,int> pii;

int abso(int a,int b)
{
	if(a<b)
		return b-a;
	else
		return a-b;
}

ll power(ll x,ll e)
{
	ll temp;
	if(e==0)
		return 1;
	if(e%2==0)
	{
		temp=power(x,e/2);
		return (temp*temp)%mod;
	}
	else
	{
		temp=power(x,e/2);
		return (((temp*temp)%mod)*x)%mod;
	}
}

bool cmp(pii x,pii y)
{
	if(x.first==y.first)
		x.second<y.second;
	x.first>y.first;
}

int a,k,n;
int st[100];
ll fans;

ll dp[55][55][55][5];

void solve(int arr[],int ind,int dist)
{
	//cout<<"ind "<<ind<<" dist "<<dist<<endl;
	/*for(int i=1;i<ind;i++)
		cout<<arr[i];
	cout<<endl;*/
	if(ind>n)
	{
		//cout<<"hello|"<<endl;
		fans++;
		if(fans>mod)
			fans%=mod;
		return ;
	}
	int flag=0,val;
	ll temp=0;
	for(int d=1;d<=a;d++)
	{	
		flag=0;
		for(int i=1;i<n;i++)
		{
			if((ind-i)<1||(ind-2*i)<1)
				break;
			else if(arr[ind-i]==d&&arr[ind-2*i]==d)
			{
				flag=1;
				break;
			}
			else
				continue;
		}
		if(flag==0)
		{
			arr[ind]=d;
			if(arr[ind]==st[ind])
				val=0;
			else
				val=1;
			if(dist+val<=k)
			{
				solve(arr,ind+1,dist+val);
			}
		}
	}
}

ll add_num(ll arr[],ll n)
{
	ll b,ans=0;
	while(n)
	{
		b=n%10;
		if(arr[b]==0)
		{
			ans++;
			arr[b]=1;
		}
		n/=10;
	}
	return ans;
}

int main()
{
	ll t,ans,dist,i,j,k,cnt;
	cin>>t;
	for(int m=1;m<=t;m++)
	{
		cin>>i;
		if(i>0)
		{
			ll arr[20];
			memset(arr,0,sizeof arr);
			k=1;
			cnt=0;
			while(cnt<10)
			{
				j=k*i;
				cnt+=add_num(arr,j);
				k++;
			}
			cout<<"Case #"<<m<<": "<<j<<endl;
		}
		else
			cout<<"Case #"<<m<<": INSOMNIA"<<endl;
	}		
	return 0;
}
