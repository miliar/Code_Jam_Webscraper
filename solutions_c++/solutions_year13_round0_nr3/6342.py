#include<stdio.h>
int main()
{
    freopen("C0.in","r",stdin);
    freopen("ATT.txt","w",stdout);
    int T,a,b,i;
    scanf("%d",&T);
    int n=1;
    while(T--)
    {
        scanf("%d%d",&a,&b);
        int num=0;
        for(i=a;i<=b;i++)
        {
            if(i==1) num++;
            if(i==4) num++;
            if(i==9) num++;
            if(i==121) num++;
            if(i==484) num++;
        }
        printf("Case #%d: %d\n",n++,num);
    }
    return 0;
}
