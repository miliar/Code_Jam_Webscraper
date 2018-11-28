#include<stdio.h>
#include<conio.h>
#include<string.h>
int main()
{
    int q;
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&q);
    int k,j;
    for(k=1;k<=q;k++)
    {
        char str[500];
        scanf(" %s",str);
        int len=strlen(str),cnt=0;
        strcat(str,"+");
        printf("Case #%d: ",k);
        for(j=0;j<len;j++)
        {
            if(str[j]!=str[j+1])
                cnt++;
        }
        printf("%d\n",cnt);
    }
    return 0;
}
