#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
using namespace std;
#define Rep(i,n) for (int i=0;i<(n);i++)
#define For(i,l,r) for (int i=(l);i<=(r);i++)
#define PB push_back
#define MP make_pair
int T,n,m,ans;
bool imp,ok;
char s[505][505];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    For(C,1,T)
    {
        scanf("%d%d",&n,&m);
        Rep(i,n)
            scanf("%s",s[i]);

//        Rep(i,n) cerr<<s[i]<<endl;

        ans=0;
        imp=false;
        Rep(i,n)
        {
            Rep(j,m)
            {
                if (s[i][j]!='.')
                {
                    ok=false;
                    for (int x=0;x<n;x++)
                        if (x!=i&&s[x][j]!='.') ok=true;

                    for (int y=0;y<m;y++)
                        if (y!=j&&s[i][y]!='.') ok=true;

                    if (!ok)
                    {
                        imp=true;
                        break;
                    }

                    ok=false;
                    if (s[i][j]=='^')
                        for (int x=0;x<i;x++)
                        if (s[x][j]!='.')
                        {
//                            cerr<<"1 i j "<<i<<" "<<j<<endl;
                            ok=true;
                        }

                    if (s[i][j]=='v')
                        for (int x=i+1;x<n;x++)
                        if (s[x][j]!='.')
                        {
//                            cerr<<"2 i j "<<i<<" "<<j<<endl;
                            ok=true;
                        }

                    if (s[i][j]=='<')
                        for (int y=0;y<j;y++)
                        if (s[i][y]!='.')
                        {
//                            cerr<<"3 i j "<<i<<" "<<j<<endl;
                            ok=true;
                        }

                    if (s[i][j]=='>')
                        for (int y=j+1;y<m;y++)
                        if (s[i][y]!='.')
                        {
//                            cerr<<"4 i j "<<i<<" "<<j<<endl;
                            ok=true;
                        }

                    if (!ok) ans++;
                }
            }
            if (imp) break;
        }
        printf("Case #%d: ",C);
        if (imp) puts("IMPOSSIBLE");
        else printf("%d\n",ans);


    }


    return 0;
}
