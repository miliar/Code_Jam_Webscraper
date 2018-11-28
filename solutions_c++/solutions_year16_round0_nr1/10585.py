#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define f first
#define s second
#define mk make_pair
#define ms(a,v) memset(a,v,sizeof(a))
using namespace std;
const int lim=1e5+5;
const int M=1e9+7;

int main()
{
  //ios_base::sync_with_stdio(false);cin.tie(NULL);
//  freopen("input.txt", "r", stdin);
  //freopen("out.txt", "w", stdout);
  
  ll i,j,t;
  cin>>t;
  
  for(j=1;j<=t;j++)
  {
  	int n,n1,k=0,a[lim],ans[lim];
  	
	bool present[12];
    ms(present,0);
    
	int cnt=0,mul=2;
	
    
  	cin>>n;
  	if(n==0)
  	{
  	  cout<<"Case #"<<j<<": ";	
  	  cout<<"INSOMNIA"<<endl;
	  continue;	
	}
	
  	n1=n;
  	
	while(n1)
  	{
  	  	a[k]=n1%10;
  	  	ans[k]=a[k];
		if( !present[a[k]] )
    	{
		 present[a[k]]=1;
		 cnt++;
		}
		
  	  	n1/=10;
  	  	k++;
	}
    int k1;
	while(cnt<10)
    {
    	int carry=0;
    	
		for(i=0;i<k;i++)
    	{
    		int cur=a[i]*mul+carry;
    		carry=cur/10;
			cur=cur%10;
			ans[i]=cur;
    		if( !present[cur] )
    		{
			 present[cur]=1;
			 cnt++;
		    }	
		}
		k1=k;
		while(carry)
		{
		
		int cur=carry%10;
		ans[k1++]=cur;
		if( !present[cur] )
    	{
		 present[cur]=1;
		 cnt++;
		}
		carry/=10;
		
	    }
	    mul++;
	}
	cout<<"Case #"<<j<<": ";
	for(i=k1-1;i>=0;i--)
	cout<<ans[i];
	cout<<endl;
  }
  return 0;
}

