#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int c,t,i,j,k,l,s;
    long long p;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d %d %d",&k,&l,&s);
        printf("Case #%d:",c+1);
        for(i=0;i<k;i++)
        {
            p=0;
            for(j=0;j<l;j++)
            {
                p=p*k+i;
            }
            printf(" %I64d",p+1);
        }
        printf("\n");
    }
    return 0;
}
