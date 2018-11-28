#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#define eps 1e-8
#define db double
#define rt return
#define cn const
#define op operator
#define N 110
using namespace std;

char c[N][N];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);

    for(int ca=1;ca<=T;ca++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        gets(c[0]);

        for(int i=0;i<n;i++)
        {
             gets(c[i]);
        }




        bool flag=true;
        int ans=0;
        for(int i=0;i<n && flag;i++)
        for(int j=0;j<m && flag;j++)
        if(c[i][j]!='.')
        {
            bool f=false;
            int cnt=0;

                for(int k=i-1;k>=0;k--)
                    if(c[k][j]!='.')
                {
                    if(c[i][j]=='^')
                    f=true;
                     cnt++;
                    break;

                }

                for(int k=j+1;k<m;k++)
                    if(c[i][k]!='.')
                {
                    if(c[i][j]=='>')
                    f=true;
                     cnt++;
                    break;
                }


                for(int k=i+1;k<n;k++)
                    if(c[k][j]!='.')
                {if(c[i][j]=='v')
                    f=true;
                    cnt++;
                    break;
                }


                for(int k=j-1;k>=0;k--)
                    if(c[i][k]!='.')
                {
                    if(c[i][j]=='<')
                       f=true;
                       cnt++;
                    break;
                }

            if(f) continue;
            if(cnt==0) flag=false;
            ans++;
        }

        printf("Case #%d: ",ca);
        if(!flag) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}

