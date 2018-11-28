#include <fstream>

using namespace std;

long long a[15][105],s[15][105],x[105],p[105],i,j,n,m;

ifstream f("in.txt");
ofstream g("out.txt");

bool prim(int x)
{
    long long d;
    for (d=2;d*d<=x;d++)
        if (x%d==0)
            return 0;
    return 1;
}

void afisare()
{
    long long i,j,v[15]={0};
    for (i=2;i<=10;i++)
    {
        for (j=1;j<=100;j++)
            if (s[i][j]==0)
            {
                v[i]=p[j];
                break;
            }
        if (v[i]==0)
            return;
    }
    for (i=n;i>=1;i--)
        g << x[i];
    for (i=2;i<=10;i++)
        g << ' ' << v[i];
    m--;
    g << "\n";
}


void back(int k)
{
    long long c[15][105],d[15][105],i,j;
    if (k==n+1)
    {
        if (x[n]==1)
            afisare();
        return;
    }
    for (i=2;i<=10;i++)
        for (j=1;j<=100;j++)
        {
            c[i][j]=a[i][j];
            a[i][j]=a[i][j]*i%p[j];
        }
    back(k+1);
    if (!m)
        return;
    for (i=2;i<=10;i++)
        for (j=1;j<=100;j++)
        {
            d[i][j]=s[i][j];
            s[i][j]=(s[i][j]+a[i][j])%p[j];
        }
    x[k]=1;
    back(k+1);
    if (!m)
        return;
    x[k]=0;
    for (i=2;i<=10;i++)
        for (j=1;j<=100;j++)
        {
            a[i][j]=c[i][j];
            s[i][j]=d[i][j];
        }
}

int main()
{
    p[1]=2;
    for (i=2;i<=100;i++)
    {
        p[i]=p[i-1]+1;
        while (!prim(p[i]))
            p[i]++;
    }
    f >> i >> n >> m;
    g << "Case #1:\n";
    x[1]=1;
    for (i=2;i<=10;i++)
        for (j=1;j<=100;j++)
        {
            a[i][j]=1;
            s[i][j]=1;
        }
    back(2);
    return 0;
}
