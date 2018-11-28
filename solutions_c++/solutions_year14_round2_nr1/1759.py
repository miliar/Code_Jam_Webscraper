#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
char s[110][110],g[110][110];
int a[110][110],b[110],med,suma,nr,t,n,ok;

int diff(int x,int y)
{
    if(x>y)
        return x-y;
    else
        return y-x;
}

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d\n",&t);
    for(int kk=1;kk<=t;kk++)
    {
        for(int i=1;i<=100;i++)
        {
            b[i]=0;
            for(int j=0;j<=100;j++)
            {
                g[i][j]=NULL;
                s[i][j]=NULL;
                a[i][j]=0;
            }
        }
        scanf("%d\n",&n);
        for(int i=1;i<=n;i++)
        {
            gets(s[i]);
            scanf("\n");
            nr=0;
            g[i][0]=s[i][0];
            a[i][nr]=1;
            for(int j=1;j<strlen(s[i]);j++)
            {
                if(s[i][j]!=s[i][j-1])
                {
                    nr++;
                    g[i][nr]=s[i][j];
                    a[i][nr]=1;
                }
                else
                {
                    a[i][nr]++;
                }
            }
        }
        ok=0;
        for(int i=2;i<=n;i++)
        {
            if(strcmp(g[i],g[1]))
            {
                ok=1;
                break;
            }
        }
        if(ok==1)
        {
            printf("Case #%d: Fegla Won\n",kk);
        }
        else
        {
            suma=0;
            for(int i=0;i<strlen(g[1]);i++)
            {
                for(int j=1;j<=n;j++)
                {
                    b[j]=a[j][i];
                }
                sort(b+1,b+n+1);
                med=b[(n+1)/2];
                for(int j=1;j<=n;j++)
                {
                    suma=suma+diff(b[j],med);
                }
            }
            printf("Case #%d: %d\n",kk,suma);
        }
    }
    return 0;
}
