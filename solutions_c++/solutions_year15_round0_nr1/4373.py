#include<stdio.h>
#include<iostream>
int main()
{
    int i,j,k,t,n,r,a;
    char s[1010];
   FILE *out;
    FILE *in;
    in=freopen("A-large.in","r",stdin);
    out=freopen("out.txt","w",stdout);
    scanf("%d",&t);

    for(i=0;i<t;i++)
    {
        scanf("%d%s",&n,&s);
        r=0;a=0;
        for(j=0;j<=n;j++)
        {
            if(s[j]=='0'&&a<(j+1))
            {
                r+=j+1-a;
                a+=j+1-a;
            }
            a+=s[j]-'0';

        }
        printf("Case #%d: %d\n",i+1,r);
    }
}
