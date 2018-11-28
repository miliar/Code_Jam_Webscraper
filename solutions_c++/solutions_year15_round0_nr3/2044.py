#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int s[5][5];
char str[150000];
int main()
{
        freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt0.txt","w",stdout);
    s[1][1]=1;
    s[1][2]=2;
    s[1][3]=3;
    s[1][4]=4;
    s[2][1]=2;
    s[2][2]=-1;
    s[2][3]=4;
    s[2][4]=-3;
    s[3][1]=3;
    s[3][2]=-4;
    s[3][3]=-1;
    s[3][4]=2;
    s[4][1]=4;
    s[4][2]=3;
    s[4][3]=-2;
    s[4][4]=-1;
    int cas,n,t;
    scanf("%d",&cas);
    for (int c=1; c<=cas; c++)
    {
        scanf("%d%d",&n,&t);
        scanf("%s",str);
        int sign=1;
        int tmp=1;
        int posi=1000000,posj=1000000;
        for (int j=0; j<t; j++)
            for (int i=0; i<n; i++)
            {
                int u=1;
                if (str[i]=='i') u=2;
                if (str[i]=='j') u=3;
                if (str[i]=='k') u=4;
                if (s[tmp][u]<0)
                    sign=sign*-1;
                tmp=abs(s[tmp][u]);

                if (tmp==2 && sign==1 && j*n+i<posi)
                    posi=j*n+i;
                if (posi!=1000000 && sign==1 && tmp==4 && j*n+i<posj)
                    posj=j*n+i;
            }
        if (sign==-1 && tmp==1 && posi!=1000000 && posj!=1000000)
        {
            printf("Case #%d: YES\n",c);
        }

        else
            printf("Case #%d: NO\n",c);
    }
    return 0;
}
