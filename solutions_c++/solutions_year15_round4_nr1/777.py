#include<stdio.h>
int a, i, j, j1, i1, rez, ok, n, m, ii, t, vs, vd, vsus, vjos;
char ma[200][200], s[200];

bool ver_stg()
{
    for (j1=1;j1<j;j1++)
        if (ma[i][j1]!='.')
            return 1;
    return 0;
}

bool ver_dr()
{
    for (j1=j+1;j1<=m;j1++)
        if (ma[i][j1]!='.')
            return 1;
    return 0;
}

bool ver_sus()
{
    for (i1=1;i1<i;i1++)
        if (ma[i1][j]!='.')
            return 1;
    return 0;
}

bool ver_jos()
{
    for (i1=i+1;i1<=n;i1++)
        if (ma[i1][j]!='.')
            return 1;
    return 0;
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%ld",&t);
    for(ii=1;ii<=t;ii++)
    {
        scanf("%ld %ld",&n,&m);
        for (i=1;i<=n;i++)
        {
            scanf("%s",s);
            for (j=0;j<m;j++)
                ma[i][j+1]=s[j];
        }
        rez=0;  ok=1;
        for (i=1;(i<=n)&&(ok);i++)
            for (j=1;(j<=m)&&(ok);j++)
                if (ma[i][j]!='.')
                {
                    vs=ver_stg();
                    vd=ver_dr();
                    vsus=ver_sus();
                    vjos=ver_jos();
                    if (((vs==0)&&(ma[i][j]=='<'))||((vd==0)&&(ma[i][j]=='>'))||((vsus==0)&&(ma[i][j]=='^'))||((vjos==0)&&(ma[i][j]=='v')))
                    {
                        rez++;
                        if (vs+vd+vsus+vjos==0)
                            ok=0;
                    }
                }
        if (ok)
            printf("Case #%ld: %ld\n",ii,rez);
        else
            printf("Case #%ld: IMPOSSIBLE\n",ii);
    }
    return 0;
}
