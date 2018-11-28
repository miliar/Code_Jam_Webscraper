#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int n,m;
long long p,q;
long long po[50]={1};
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int tit,tot;
    for(int i=1;i<50;i++)po[i]=po[i-1]*2;
    for(scanf("%d",&tot),tit=1;tit<=tot;tit++)
    {
        scanf("%I64d/%I64d",&p,&q);
        if(po[40]*p%q)
            printf("Case #%d: impossible\n",tit);
        else
        {
            int i=0;
            for(i=1;1;i++)
                if(po[i]*p>=q)
                    break;
            printf("Case #%d: %d\n",tit,i);
        }
    }
	return 0;
}
