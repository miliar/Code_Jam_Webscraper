#include<bits/stdc++.h>
using namespace std;
#define ll long long 
int main()
{
	ll s,i,j;
	char a[1004];
	ll sum ;
	ll ans;
    ll t;
    
    FILE *fp,*fp1;
	
	fp=freopen("A-large.in","r",stdin);
	fp1=freopen("out1.text","w+",stdout);

    scanf("%lld",&t);
    
    for(j=1;j<=t;j++)
    {
    	scanf("%lld",&s);
    	scanf("%s",a);
    	sum=0;ans=0;
    	for(i=0;i<=s;i++)
    	  {
    	    a[i]=a[i]-'0';
    	  	if(a[i]==0)
    	  	{
		//	printf("%lld\n",ans);
         	    continue ;
    	  }
			else 
    	  	{
    	  	    if(sum<i)
				  {
				  	 ans+=(i-sum);
					 sum+=(i-sum);	
				  }	
				   sum+=a[i];
			}
		//	printf("%lld\n",ans);

		  }
		  printf("Case #%lld: %lld\n",j,ans);
	}
	fclose(stdin);
    fclose(stdout);
	return 0;
}
