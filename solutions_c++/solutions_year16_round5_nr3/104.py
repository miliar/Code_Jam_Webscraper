#include <bits/stdc++.h>
using namespace std;

int t;

int n;
int s;

int x[1007];
int y[1007];
int z[1007];

int vx[1007];
int vy[1007];
int vz[1007];

double pocz[1007][1007];
double kon[1007][1007];

double bsa, bsb, bss;

double tsa, tsb, tss1, tss2;
double ba, bb, bs;

double inf=10000000.0;

int bylo[1007][1007];
int zwr;

inline double xpo(int v, double t)
{
    return x[v]+t*vx[v];
}

inline double ypo(int v, double t)
{
    return y[v]+t*vy[v];
}

inline double zpo(int v, double t)
{
    return z[v]+t*vz[v];
}

inline double kwa(double v)
{
    return v*v;
}

inline double odlpo(int v, int u, double t)
{
    return sqrt(kwa(xpo(v, t)-xpo(u, t))+kwa(ypo(v, t)-ypo(u, t))+kwa(zpo(v, t)-zpo(u, t)));
}

inline int zero(double v)
{
    return abs(v)<0.000000001;
}

inline void dfs(int v, int u)
{
    if (zwr)
    return;
    if (v>u)
    swap(v, u);
    if (bylo[v][u])
    return;
    bylo[v][u]=1;
    //printf("%d %d\n", v, u);
    if (v==2 || u==2)
    {
        zwr=1;
        return;
    }
    for (int i=1; i<=n; i++)
    {
        if (kon[v][u]+s<pocz[u][i] || kon[u][i]+s<pocz[v][u] || kon[u][i]<0.0)
        continue;
        dfs(u, i);
    }
    for (int i=1; i<=n; i++)
    {
        if (kon[v][u]+s<pocz[v][i] || kon[v][i]+s<pocz[v][u] || kon[v][i]<0.0)
        continue;
        dfs(v, i);
    }
}

int check()
{
    for (int i=1; i<=n; i++)
    {
        for (int j=1; j<=i; j++)
        {
            if ( zero(odlpo(i, j, 0.0)-odlpo(i, j, 1.0)) && zero(odlpo(i, j, 0.0)-odlpo(i, j, 2.0)) && zero(odlpo(i, j, 0.0)-odlpo(i, j, 3.0)) )
            {
                if (odlpo(i, j, 0.0)>bss)
                {
                    pocz[i][j]=-1.0;
                    kon[i][j]=-1.0;
                }
                else
                {
                    pocz[i][j]=0.0;
                    kon[i][j]=1000000.0;
                    kon[i][j]*=kon[i][j];
                }
                pocz[j][i]=pocz[i][j];
                kon[j][i]=kon[i][j];
                continue;
            }

            tsa=0.0;
            tsb=1000000000.0;
            for (int h=1; h<=70 && tsa<tsb; h++)
            {
                tss1=tsa+(tsb-tsa)*2.0/5.0;
                tss2=tsa+(tsb-tsa)*3.0/5.0;
                if (odlpo(i, j, tss1)<odlpo(i, j, tss2))
                {
                    tsb=tss2;
                }
                else
                {
                    tsa=tss1;
                }
            }
            if (odlpo(i, j, tsa)>bss)
            {
                pocz[i][j]=-1.0;
                kon[i][j]=-1.0;
                pocz[j][i]=pocz[i][j];
                kon[j][i]=kon[i][j];
                continue;
            }
            ba=0.0;
            bb=1000000000.0;
            for (int h=1; h<=50 && ba<bb; h++)
            {
                bs=(ba+bb)/2.0;
                if (odlpo(i, j, tsa-bs)>bss)
                {
                    bb=bs;
                }
                else
                {
                    ba=bs;
                }
            }
            pocz[i][j]=tsa-ba;
            ba=0.0;
            bb=1000000000.0;
            for (int h=1; h<=50 && ba<bb; h++)
            {
                bs=(ba+bb)/2.0;
                if (odlpo(i, j, tsa+bs)>bss)
                {
                    bb=bs;
                }
                else
                {
                    ba=bs;
                }
            }
            kon[i][j]=tsa+ba;

            if (kon[i][j]<0.0)
            {
                pocz[i][j]=-1.0;
                kon[i][j]=-1.0;
                pocz[j][i]=pocz[i][j];
                kon[j][i]=kon[i][j];
                continue;
            }

            pocz[i][j]=max(pocz[i][j], 0.0);

            pocz[j][i]=pocz[i][j];
            kon[j][i]=kon[i][j];
        }
    }
    pocz[1][1]=0.0;
    kon[1][1]=0.0;
    for (int i=1; i<=n; i++)
    {
        for (int j=1; j<=n; j++)
        {
            //printf("z %d do %d   %lf-%lf\n", i, j, pocz[i][j], kon[i][j]);
            bylo[i][j]=0;
        }
    }
    zwr=0;
    dfs(1, 1);
    return zwr;
}

int main()
{
    scanf("%d", &t);
    for (int tt=1; tt<=t; tt++)
    {
        cerr << tt << endl;
        printf("Case #%d: ", tt);
        scanf("%d%d", &n, &s);
        for (int i=1; i<=n; i++)
        {
            scanf("%d%d%d", &x[i], &y[i], &z[i]);
            scanf("%d%d%d", &vx[i], &vy[i], &vz[i]);
        }
        bsa=0.0;
        bsb=3000.0;
        for (int h=1; h<=45 && bsa<bsb; h++)
        {
            bss=(bsa+bsb)/2;
            if (check())
            {
                bsb=bss;
            }
            else
            {
                bsa=bss;
            }
        }
        printf("%.6lf\n", bsa);
    }
    return 0;
}
