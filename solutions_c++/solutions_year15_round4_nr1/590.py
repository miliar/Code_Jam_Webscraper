#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
using namespace std;
char s[106][106];
main()
{
    freopen("A-large (2).in","r",stdin);
    freopen("A-large (2).out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
        scanf("%s",s[i]);
        int ans=0,f=1;
        for(int i=0;(i<n)&&f;i++)
        for(int j=0;(j<m)&&f;j++) if(s[i][j]!='.')
        {
            int a=1,b=1,c=1,d=1;
            for(int k=0;k<j;k++) if(s[i][k]!='.')
            {
                a=0;break;
            }
            for(int k=j+1;k<m;k++) if(s[i][k]!='.')
            {
                b=0;break;
            }
            for(int k=0;k<i;k++) if(s[k][j]!='.')
            {
                c=0;break;
            }
            for(int k=i+1;k<n;k++) if(s[k][j]!='.')
            {
                d=0;break;
            }
            if(a+b+c+d==4) {f=0;break;}
            if(s[i][j]=='<'&&a==1) ans++;
            if(s[i][j]=='>'&&b==1) ans++;
            if(s[i][j]=='^'&&c==1) ans++;
            if(s[i][j]=='v'&&d==1) ans++;

        }
        printf("Case #%d: ",++cas);
        if(!f) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
}
