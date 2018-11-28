#include<stdio.h>
#include<math.h>
int main()
{
    //freopen("C0.in","r",stdin);
    //freopen("C0.txt","w",stdout);
    int T,q,m,n,cont;
    scanf("%d",&T);
    for(q=1;q<=T;q++)
    {
        scanf("%d%d",&n,&m);cont=0;
        printf("Case #%d: ",q);
        if(1>=n&&1<=m) cont++;
        if(4>=n&&4<=m) cont++;
        if(9>=n&&9<=m) cont++;
        if(121>=n&&121<=m) cont++;
        if(484>=n&&484<=m) cont++;
        printf("%d\n",cont);
    }
    return 0;
}
