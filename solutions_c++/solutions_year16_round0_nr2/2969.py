#include<stdio.h>
#include<stdlib.h>
#include<string.h>
main()
{
     int ttt;
    scanf("%d",&ttt);
    for(int tt=0;tt<ttt;tt++)
    {
        printf("Case #%d: ",tt+1);
        char a[120];
        scanf("%s",a);
        int s = strlen(a);
        strcat(a,"+");
        int cnt=0;
        for(int i=0;i<s;i++)
        {
            if(a[i]!=a[i+1])cnt++;
        }
        printf("%d\n",cnt);
    }
}
