#include<stdio.h>
int main()
{
    int n,a,b,i,p=1;
//    freopen("C0.in","r",stdin);
//    freopen("C00.in","w",stdout);
    scanf("%d",&n);
    while(n--)
    {
        scanf("%d%d",&a,&b);
        printf("Case #%d: ",p++);
        int sum=0;
        for(i=a;i<=b;i++)
        {
            if(i==1||i==4||i==9||i==121||i==484)
                sum++;
        }
        printf("%d\n",sum);
    }
}
