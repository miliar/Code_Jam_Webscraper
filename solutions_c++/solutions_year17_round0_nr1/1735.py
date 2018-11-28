#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

char s[1<<10];
int n,k;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int c,t,i,j,ans;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%s %d",s,&k);
        n=strlen(s);
        ans=0;
        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                if(i+k>n)
                {
                    ans=-1;
                    break;
                }
                ans++;
                for(j=i;j<i+k;j++)
                {
                    if(s[j]=='-')
                    {
                        s[j]='+';
                    }
                    else
                    {
                        s[j]='-';
                    }
                }
            }
        }
        printf("Case #%d: ",c+1);
        if(ans!=-1)
        {
            printf("%d\n",ans);
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
