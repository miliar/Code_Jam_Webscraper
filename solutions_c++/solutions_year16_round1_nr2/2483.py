#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <cmath>
using namespace std;
int n,m;
int num[2502];
int T;
int main()
{
//    freopen("B.in","r",stdin);
//    freopen("B.out","w",stdout);
    
    scanf("%d",&T);
    for(int ii=1;ii<=T;++ii)
    {
        scanf("%d",&n);
        memset(num,0,sizeof(num));
        for(int i=1;i<2*n;++i)
        {
            for(int j=1;j<=n;++j)
            {
                int x;
                scanf("%d",&x);
                num[x]^=1;
            }
        }
        printf("Case #%d:",ii);
        for(int i=1;i<=2500;++i)
        {
            if(num[i])printf(" %d",i);
        }
        printf("\n");
    }
    return 0;
}