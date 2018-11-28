#include<bits/stdc++.h>

using namespace std;
int t,i,j,k,l,n,ans,x,f;
char c[105],d[105];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        ans=0;
        scanf("%s",c);
        n=strlen(c);
        memset(d,0,sizeof(d));
        for(i=0;i<n;i++)
        {
            d[i]='+';
        }
        while(strcmp(c,d)!=0)
        {
            for(i=n-1;i>=0;i--)
            {
                if(c[i]=='-')
                {
                    x=i+1;
                    break;
                }
            }
            f=0;
            for(i=0;i<n;i++)
            {
                if(c[i]=='-')
                {
                    break;
                }
                else
                {
                    f=1;
                    c[i]='-';
                }
            }
            if(f==1)
            {
                ans++;
            }
            reverse(c,c+x);
            ans++;
            for(i=0;i<x;i++)
            {
                if(c[i]=='+')
                {
                    c[i]='-';
                }
                else
                {
                    c[i]='+';
                }
            }
        }
        printf("Case #%d: %d\n",l,ans);
    }
    return 0;
}
