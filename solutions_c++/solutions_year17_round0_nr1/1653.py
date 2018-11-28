#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t,n,ans,len,tag[1234];
    char s[1234];
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%s%d",s,&n);
        memset(tag,0,sizeof(tag));
        ans=0;
        len=strlen(s);
        for (int i=0,flag=0;i<len;++i)
        {
            flag^=tag[i];
            if ((flag^(s[i]=='+'?0:1))==1)
            {
                if (i+n>len)
                {
                    ans=-1;
                    break;
                }
                flag^=1;
                ++ans;
                tag[i+n]=1;
            }
        }
        printf("Case #%d: ",cas);
        if (ans==-1) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
