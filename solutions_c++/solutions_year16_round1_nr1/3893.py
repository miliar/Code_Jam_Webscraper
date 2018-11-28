#include<iostream>
using namespace std;
#include<cstdio>
#include<string.h>
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    char s[3000],ch,temp[3000];
    int t,beg,last,len,i,j;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%s",s);
        len=strlen(s);
        beg=last=len;
        temp[beg]=s[0];
        for(j=1;s[j]!='\0';j++)
        {
            if(s[j]>=temp[beg])
            {
                beg--;
                temp[beg]=s[j];
            }
            else
            {
                temp[++last]=s[j];
            }
        }
        printf("Case #%d: ",i);
        for(j=beg;j<=last;j++)
            printf("%c",temp[j]);
        printf("\n");
    }
    return 0;
}

