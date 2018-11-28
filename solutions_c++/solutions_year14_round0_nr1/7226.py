#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int n,m;
int a[16],h[17];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int tit,tot;
    for(scanf("%d",&tot),tit=1;tit<=tot;tit++)
    {
        scanf("%d",&n);
        for(int i=0;i<16;i++)
            scanf("%d",&a[i]),h[i+1]=0;
        for(int i=n*4-4;i<n*4;i++)
            h[a[i]]++;
            
        scanf("%d",&n);
        for(int i=0;i<16;i++)
            scanf("%d",&a[i]);
        for(int i=n*4-4;i<n*4;i++)
            h[a[i]]++;
        int ans=0,ansj;
        for(int i=1;i<=16;i++)
            if(h[i]>=2)
                ans++,ansj=i;
        if(ans==0)printf("Case #%d: Volunteer cheated!\n",tit);
        else if(ans>1)printf("Case #%d: Bad magician!\n",tit);
        else printf("Case #%d: %d\n",tit,ansj);
    }
	return 0;
}
