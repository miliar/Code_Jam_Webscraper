#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define lldd long long int
#define mod 1000000007
using namespace std;
int main()
{
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int tt=t;
	while(t--)
	{
		int s;
		scanf("%d",&s);
		char a[s+2];
		scanf("%s",a);
	    int cum =a[0]-'0';
	    lldd ans=0;
	    for(int i=1;i<s+1;i++)
	    {
	    	if(cum<i)
	    	{
	    		ans+=(i-cum);
	    	    cum+=(i-cum);
	    	}
	    		cum+=a[i]-'0';
	    }
	    printf("Case #%d: %lld\n",tt-t,ans);
	}
}