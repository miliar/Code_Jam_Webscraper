#include "stdio.h"
char c[15];
void bi(int num)
{
    c[14]='\0';
    for(int i=13;i>=0;i--)
    {
        c[i]='0'+num%2;
        num/=2;
    }
    printf("%s",c);
}
main()
{
    freopen("C-Large.in","r",stdin);
    freopen("C-L.txt","w",stdout);
    int w,i;
    scanf("%d %d %d",&w,&w,&w);
    printf("Case #1:\n");
    for(i=0;i<500;i++)
    {
        printf("1");
        bi(i);
        printf("11");
        bi(i);
        printf("1 65537 2 641 2 353 2 193 2 353\n");
    }
}
