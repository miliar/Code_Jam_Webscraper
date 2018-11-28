#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
#define inf 1000000
int dp[105][105];
int suf[105],len;
string str;
int cal(int pos,int pr)
{
	    if(pr+suf[pos]==len)
	    {
	    	return 0;
		}
		// cout<<pos<<" "<<pr<<endl;
	    if(pos>=len)
	    {
		 if(pr+suf[pos]==len)
		    {
		    	return 0;
			}
			else
		 return inf;
		}
	    
	    if(dp[pos][pr]!=-1)
	    return dp[pos][pr];
		
		int i,cnt,tot,tmp;
		int r1;
		r1 = inf;
		cnt = 0;
		tmp = pos-pr;
	    for(i=pos;i<len;i++)
	    {
	    	if(str[i]=='-')
	    	{
	    		cnt++;
			}
				tot = cnt+tmp;
			r1 = min(r1,1+cal(i+1,tot));	
		}
	    
	    return dp[pos][pr]=r1;
	
}

int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
	int tcase,t,i;
	scanf("%d",&tcase);
	for(t=1;t<=tcase;t++)
	{
		cin>>str;
		len = str.size();
		suf[len] = 0;
		for(i=len-1;i>=0;i--)
		{
			if(str[i]=='+')
			{
				suf[i]=suf[i+1]+1;;
			}
			else
			{
				suf[i] = suf[i+1];
			}
		}
		memset(dp,-1,sizeof dp);
	   printf("Case #%d: %d\n",t,cal(0,0));
	}
}

