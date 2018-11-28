#include<cstdio>
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
char s[105];
main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        int n,l;scanf("%d%d",&n,&l);
        int ch=0;
        for(int i=0;i<n;i++)
        {
            scanf("%s",s);
            int ct=0;
            for(int j=0;j<l;j++) ct+=s[j]-'0';
            if(ct==l) ch=1;
        }
        scanf("%s",s);
        printf("Case #%d: ",++cas);
        if(ch==1)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        for(int i=0;i<l;i++) printf("?0");
        printf(" 0");
        for(int i=0;i<l-1;i++) printf("10");
        printf("\n");

    }
}
