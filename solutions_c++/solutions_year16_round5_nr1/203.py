#include<cstdio>
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
char s[20005];
main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        scanf("%s",s);
        int n=strlen(s);
        int ans=0;
        while(1)
        {
            int f=0,cur=0;
            for(int i=0;i<n;i++)
            {
                if(s[i]==s[i+1])
                {
                    ans+=10;
                    f=1;i++;
                }
                else
                {
                    s[cur++]=s[i];
                }
            }
            s[cur]='\0';
            n=cur;
            if(f==0) break;
        }
        ans+=n/2*5;
        printf("Case #%d: %d\n",++cas,ans);

    }
}
