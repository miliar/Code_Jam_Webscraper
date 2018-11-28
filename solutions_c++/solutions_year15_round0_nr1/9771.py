#include<stdio.h>
using namespace std;
int main()
{
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("A-small-attempt0.out","w",stdout);
    char a[2000];
    int i,j,k,l,t,s;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%d",&s);
        scanf("%s",a);
        for(i=0,k=0,l=0;i<=s;i++)
        {
            if(i<=k)k+=(a[i]-48);
            else if(a[i]!='0')
            {
//                printf("%d %d\n",i,k);
                l+=(i-k);
                k+=(a[i]-48)+l;
            }
        }
        printf("Case #%d: %d\n",j,l);
    }
    return 0;
}
