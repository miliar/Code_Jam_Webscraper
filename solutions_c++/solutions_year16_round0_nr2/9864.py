#include<cstdio>
#include<iostream>
#include<cstring>
#define clr(x) memset(x,0,sizeof(x))
using namespace std;
char s[200];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int n,sum,ct;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%s",s);
        sum=0;
        if(s[0]=='-')
            sum=1;
        for(int j=1;j<strlen(s);j++)
            if(s[j]=='-'&& s[j-1]=='+')
            sum+=2;
        printf("Case #%d: %d\n",i,sum);
    }
    return 0;

}
