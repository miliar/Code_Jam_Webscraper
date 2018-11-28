#include<stdio.h>
#include<string.h>
char s[1010];
char a[1010];
char b[1010];
char c[1010];
void doit()
{
    scanf("%s",s);
    int n = strlen(s);
    a[0] = 0;
    for(int i=0;i<n;i++)
    {
        strcpy(b,a);
        strcpy(c+1,a);
        c[0] = s[i];
        b[i] = s[i];
        c[i+1] = 0;
        b[i+1] = 0;
        if(strcmp(b,c) >0)
        {
            strcpy(a,b);
        }else
        {
             strcpy(a,c);
        }
    }
    printf("%s\n",a);
}
int main()
{
    int t;
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
         printf("Case #%d: ",i);doit();
    }
}
