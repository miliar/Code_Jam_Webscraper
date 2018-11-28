#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
#define inf 100000000000000000

bool vis[20];
int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
	ll i,j,num,tmp,len,cnt,k,t,tcase;
	scanf("%lld",&tcase);
	for(t=1;t<=tcase;t++)
	{
	    scanf("%lld",&num);
	   
		for(j=0;j<11;j++)
		vis[j] = 0;
		
		cnt = 0;
		if(num!=0)
		for(j=1;;j++)
		{
	       tmp = num*j;
		   string str;
		   ostringstream strs;
		   
		   strs<<tmp;
		   str = strs.str();
		   len = str.size();
		   for(k=0;k<len;k++)
		   {
		       if(vis[str[k]-'0']==0)
			   {
			      cnt++;
				  vis[str[k]-'0'] = 1;	
			   }	
			   
		   }
		   if(cnt==10)
			   break;	
		}
		if(num==0)
		{
			printf("Case #%lld: INSOMNIA\n",t);
		}
		else
		    printf("Case #%lld: %lld\n",t,tmp);
	}
	
	
}

