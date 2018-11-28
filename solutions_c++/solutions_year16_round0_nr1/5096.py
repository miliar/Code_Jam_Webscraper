#include<bits/stdc++.h>

using namespace std;
#define ll long long 
int main()
{ 
    freopen("A-large.in","r",stdin);
    freopen("output1.txt","w",stdout);	 
	 ll t,n;
	 cin>>t;
	  for(int z=1;z<=t;z++)
	 { int cnt[10];
	   for(int i=0;i<10;i++)
	      cnt[i]=0;
	   
	   ll sum=0;
	   int flag=1;
	   cin>>n;
	   if(n==0)
	    {
	    	flag=0;
	    	sum=11;
		}
	   ll start=1;
	    while(sum<10)
	    {
	      ll i=n*start;
	    	
	    	while(i>0)
	    	{
	    		ll rem=i%10;
	    		i=i/10;
	    		if(cnt[rem]==0)
	    		{
	    			cnt[rem]++;
	    			sum++;
				}
			}
			start++;
		}
	    ll ans=n*(start-1);
	    if(flag)
	 	cout<<"Case #"<<z<<": "<<ans<<endl;
	 	else
	 	cout<<"Case #"<<z<<": "<<"INSOMNIA"<<endl;
	 	
	  } 
}
