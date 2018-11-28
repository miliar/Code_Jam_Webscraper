#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#define MAXN 1020
using namespace std;
int a[MAXN];
int main(){
    freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    int T,D,m,ans,count;
    scanf("%d",&T);
    for(int tt=1;tt<=T;++tt)
	{
        scanf("%d",&D);
        for(int i=0;i<D;i++)
            scanf("%d",&a[i]);
        sort(a,a+D);
        m=a[D-1];
        ans=a[D-1];
        for(int k=1;k<=m;k++)
		{
            count=k;
            for(int i=D-1;i>=0;i--)
			{
                if(a[i]<k)break;
                count+=ceil((double)a[i]/k)-1;  
            }
        	ans=min(ans,count);
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}

