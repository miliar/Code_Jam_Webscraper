#include<stdio.h>
#include<string.h>
char s[105];
void doit()
{
    scanf("%s",s);
    int len = strlen(s);
    int temp = len;
    for(int i=1;i<temp;i++)
        if(s[i-1] == s[i])
            len--;
    if(s[0] == '-')
    {
        if(len%2 == 1) printf("%d\n",len);
        else printf("%d\n",len-1);
    }else
    {
        if(len%2 == 1) printf("%d\n",len-1);
        else printf("%d\n",len);
    }
}
int main()
{
    int t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        printf("Case #%d: ",i+1);
        doit();
    }
}
