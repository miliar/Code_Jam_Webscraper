//HighFlow
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <fstream>
#include <string.h>
#include <math.h>
#include <algorithm>
#define fcat(c) while (c!='\n') fscanf(f,"%c",&c)
#define cat(c) while (c!='\n') scanf("%c",&c)
#define For(i,st,dr,k) for (int i=(st);i<=(dr);i+=(k))
#define ll (long long)
#define kfl(i,j) (a[(i)][(j)].c-a[(i)][(j)].f)
using namespace std;
FILE *f,*g;
int  i,j,k,n,m,t,q;
int a[110][110];

void solve()
{
    int i,j;
    bool ok1,ok2,ok;

    ok=true;

    for (i=1;i<=n;i++)
        for (j=1;j<=m;j++)
        {
            ok1=ok2=true;
            for (k=1;k<=n;k++)
                if (a[k][j]>a[i][j]) ok1=false;
            for (k=1;k<=m;k++)
                if (a[i][k]>a[i][j]) ok2=false;
            ok=ok&( ok1 | ok2);
        }
    if (ok)
        fprintf(g,"Case #%d: YES\n",q);
    else
        fprintf(g,"Case #%d: NO\n",q);
}

int main()
{
    f=fopen("b.in","r");
    g=fopen("b.out","w");

    fscanf(f,"%d",&t);

    for (q=1;q<=t;q++)
    {
        fscanf(f,"%d%d",&n,&m);
        for (i=1;i<=n;i++)
            for (j=1;j<=m;j++)
                fscanf(f,"%d",&a[i][j]);
        solve();
    }

	return 0;
}
