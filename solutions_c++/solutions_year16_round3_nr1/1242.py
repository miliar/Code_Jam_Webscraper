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
 

	int a[100],b[100];
int main()
{
	

       freopen("A-large.in","r",stdin);
       freopen("output_accept.txt","w",stdout);

 int t;
  cin>>t;
  
     for(int z=1;z<=t;z++)
  {	
    int n ;
      cin>>n;
      
      for(int i=0;i<n;i++)
      {
      	cin>>a[i];
      	 b[i]=a[i];
	  }
	  cout<<"Case  #"<<z<<": "; 
	  sort(b,b+n);
	  if(n==2)
	  {
	  	for(int i=0;i<a[0];i++)
	  	{
	  		cout<<"AB  ";
		  }
		  cout<<endl;
	  }
	  else
	  {
	  for(int i=b[n-1];i>=1;i--)
	  {
	  	
	  	
	    for(int j=0;j<n;j++)
	  	{
	  		   if(a[j]>i)
	  		   {
	  		    a[j]--;
	  		    cout<<char(j+65)<<"  ";
	  		  }
		  }	  
       }
       
       
       
       
	
	  for(int i=0;i<n-2;i++)
	  {
	  	 if(a[i]>0)
	  		   {
	  		    a[i]--;
	  		    cout<<char(i+65)<<"  ";
	  		  }
	  	
	  }
	   cout<<char(n-2+65)<<char(n-1+65);
       cout<<endl;
      }
  }
  
  return 0;
  
  }

	

