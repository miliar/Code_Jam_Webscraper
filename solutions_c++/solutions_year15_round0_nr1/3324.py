#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define maxn 10000

char si[maxn];

int main()
{
    int S,T,casen=0,tot,ans,i;
    scanf("%d",&T);
    while(T--)
    {
	ans=tot=0;
	scanf("%d%s",&S, si);
        for(i=0;si[i];i++)
	{
	    if(tot>=i)
		tot+=si[i]-'0';
	    else
	    {
		ans=ans + i-tot;
		tot=i + si[i]-'0';
	    }
	}
	printf("Case #%d: %d\n", ++casen, ans);
    }
    return 0;
}
