#include <stdio.h>
int main()
{
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int tt=t;
	while(t--)
	{
		int n;
		scanf("%d",&n);
		char a[n+2];
		scanf("%s",a);
	    int cum =a[0]-'0';
	    long long int ans=0;
	    for(int i=1;i<n+1;i++)
	    {
	    	if(cum<i && (a[i]-'0')!=0)
	    	{
	    		ans+=(i-cum);
	    	    cum+=(i-cum);
	    	}
	    		cum+=a[i]-'0';
	    }
	    printf("Case #%d: %lld\n",tt-t,ans);
	}
}