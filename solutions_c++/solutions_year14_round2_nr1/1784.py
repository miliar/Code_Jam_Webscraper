#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

int fuck[110],num[110][110],temp[110];

char str[110][110];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int n,i,j,l,cao,tot,flag=0,k,ans=0;
        scanf("%d",&n);
        for(i=1;i<=n;i++)
            scanf("%s",str[i]+1);
        l=strlen(str[1]+1);
        fuck[1]=str[1][1]-'a';
        int now=1,pre=1;
        for(i=2;i<=l;i++)
        {
           // printf("%c %c\n",str[1][i],str[1][i-1]);
            if(str[1][i]!=str[1][i-1])
            {
           //     printf("%d %d %d\n",i,pre,now);
                num[1][now]=i-pre;
                fuck[++now]=str[1][i]-'a';
                pre=i;
            }
        }
        num[1][now]=l+1-pre;
    //    printf("%d\n",now);
   //     for(i=1;i<=now;i++)
   //     {
   //         printf("%d %d\n",fuck[i],num[1][i]);
   //     }
        for(i=2;i<=n;i++)
        {
            temp[1]=str[i][1]-'a';
            tot=1;
            l=strlen(str[i]+1);
            pre=1;
            for(j=2;j<=l;j++)
            {
                if(str[i][j]!=str[i][j-1])
                {
                    num[i][tot]=j-pre;
                    temp[++tot]=str[i][j]-'a';
                    pre=j;
                }
            }
            num[i][tot]=l+1-pre;
            if(tot!=now)
            {
                flag=1;
                break;
            }
            for(j=1;j<=tot;j++)
            {
                if(temp[j]!=fuck[j])
                {
                    flag=1;
                    break;
                }
            }
            if(flag==1)
                break;
        }
    /*
        for(i=1;i<=n;i++)
            for(j=1;j<=now;j++)
                printf("%d %d %d\n",i,j,num[i][j]);
    */
        if(flag==1)
            printf("Case #%d: Fegla Won\n",++cas);
        else
        {
            for(i=1;i<=now;i++)
            {
                int maxx=0;
                for(j=1;j<=n;j++)
                    maxx=max(maxx,num[j][i]);
                int minn=1000;
                for(j=1;j<=maxx;j++)
                {
                    cao=0;
                    for(k=1;k<=n;k++)
                        cao=cao+abs(num[k][i]-j);
                    if(cao<minn)
                        minn=cao;
                }
                ans=ans+minn;
            }
            printf("Case #%d: %d\n",++cas,ans);
        }
    }
    return 0;
}
