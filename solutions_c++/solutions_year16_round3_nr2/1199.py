#include<bits/stdc++.h>
 
#define MOD 1000000007
#define MAX 1000
#define ll long long 
#define slld(t) scanf("%lld",&t)
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define plld(t) printf("%lld\n",t)
#define pcc pair<char,char>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define mp(a,b) make_pair(a,b)
#define F first
#define S second
#define pb(x) push_back(x)

using namespace std;
 

	int a[100][100];
int main()
{
	

    freopen("B-small-attempt1.in","r",stdin);
    freopen("output_accept.txt","w",stdout);

 int t;
  cin>>t;
  
     for(int z=1;z<=t;z++)
  {	
    ll n , m ;
    cin>>n>>m;
    ll temp= 1 << (n-2);
    cout<<"Case #"<<z<<": ";
    if(temp<m)
    {
    	cout<<"IMPOSSIBLE"<<endl;
    		}
	else
	{
		
		for(int i=0;i<n-1;i++)
		{
			for(int j=0;j<n-1;j++)
			  {
			  	if(j>i)
			  	  a[i][j]=1;
					  else
					     a[i][j]=0;		
			  }
		}
		
		for(int j=0;j<n;j++)
		{
			a[n-1][j]=0;
			a[j][n-1]=0;
		}
		
		if(temp==m)
		{
			for(int i=0;i<n-1;i++)
			  a[i][n-1]=1;
		}
		else
		{int start=1;
		   while(start< n-1)
		   {
		   	if(m%2==1)
		   	  a[start][n-1]=1;
		   	  m=m/2;
		   	  start++;
		   }	     
		}
		
		cout<<"POSSIBLE"<<endl;
		
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			  cout<<a[i][j];
			  
			  cout<<endl;
		}
		
		
	}
	
	
}
  return 0;
  
  }

	

