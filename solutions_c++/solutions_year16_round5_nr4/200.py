
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

int n,L;
char s[300];

int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int T,Tt=0;scanf("%d",&T);
    for (;T--;)
    {
        scanf("%d%d",&n,&L);
        bool Pp=0;
        for (int i=1;i<=n;i++)
        {
            scanf("%s",s+1);
            bool P=1;    
            for (int j=1;j<=L;j++)
                if (s[j]!='1') P=0;
            Pp|=P;
        }
        scanf("%s",s+1);
        if (Pp)
        {
            printf("Case #%d: IMPOSSIBLE\n",++Tt);
            continue;
        }
        printf("Case #%d: ",++Tt);
        if (L==1)
            puts("0 ?");
            else    {
                        for (int i=1;i<L;i++) printf("?");
                        putchar(' ');
                        printf("10?");
                        for (int i=3;i<=L;i++) printf("10");
                        putchar('1');
                    }
        puts("");
    }
}