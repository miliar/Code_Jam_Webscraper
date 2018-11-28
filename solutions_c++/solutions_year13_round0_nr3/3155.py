#include <iostream>
#include <stdio.h>
using namespace std;
int cas,k,a,b,i,cnt;
int main()
{
//    freopen("C-small-attempt4.in","r",stdin);
//    freopen("out.txt","w",stdout);
    scanf("%d",&cas);
    for (k=1; k<=cas; k++)
    {
        scanf("%d%d",&a,&b);
        cnt=0;
        for (i=a; i<=b; i++)
        {
            if (i==1||i==4||i==9||i==121||i==484)
                cnt++;
        }
        printf("Case #%d: %d\n",k,cnt);
    }
    return 0;
}
