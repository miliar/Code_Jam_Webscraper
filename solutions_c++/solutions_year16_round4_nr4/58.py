#include <bits/stdc++.h>
using namespace std;

int t;

int n;

char wcz[27][27];

int wyn;

vector <int> graf1[27];
vector <int> graf2[27];

int bylo1[27];
int bylo2[27];

vector < pair <int,int> > wek;
vector < pair < pair <int,int> , int > > wek2;

int l1, l2;

int inf=10000000;

map < vector <int> , int> mapa;

void dfs2(int v);

void dfs1(int v)
{
    if (bylo1[v])
    return;
    bylo1[v]++;
    l1++;
    for (int i=0; i<graf1[v].size(); i++)
    dfs2(graf1[v][i]);
}

void dfs2(int v)
{
    if (bylo2[v])
    return;
    bylo2[v]++;
    l2++;
    for (int i=0; i<graf2[v].size(); i++)
    dfs1(graf2[v][i]);
}

vector <int> gor, dol;

void check()
{
    /*printf("z:\n");
    for (int i=0; i<wek2.size(); i++)
    printf("%d ", gor[i]);
    printf("\n");
    printf("do:\n");
    for (int i=0; i<wek2.size(); i++)
    printf("%d ", dol[i]);
    printf("\n");*/

    int suma1=0, suma2=0;
    for (int i=0; i<wek2.size(); i++)
    {
        suma1+=(gor[i]-dol[i])*wek2[i].first.first;
        suma2+=(gor[i]-dol[i])*wek2[i].first.second;
    }
    if (suma1==suma2)
    {
        //printf("tak\n");
        mapa[gor]=min(mapa[gor], mapa[dol]+suma1*suma2);
    }
}

void rek(int v)
{
    if (v==wek2.size())
    {
        check();
        return;
    }
    for (int i=0; i<=wek2[v].second; i++)
    {
        for (int j=0; j<=i; j++)
        {
            dol.push_back(j);
            gor.push_back(i);
            rek(v+1);
            gor.pop_back();
            dol.pop_back();
        }
    }
}

int main()
{
    scanf("%d", &t);
    for (int tt=1; tt<=t; tt++)
    {
        printf("Case #%d: ", tt);
        scanf("%d", &n);
        wyn=0;
        wek.clear();
        for (int i=1; i<=n; i++)
        {
            graf1[i].clear();
            graf2[i].clear();
            bylo1[i]=0;
            bylo2[i]=0;
        }
        for (int i=1; i<=n; i++)
        {
            scanf("%s", wcz[i]+1);
            for (int j=1; j<=n; j++)
            {
                if (wcz[i][j]=='1')
                {
                    graf1[i].push_back(j);
                    graf2[j].push_back(i);
                    wyn--;
                }
            }
        }
        for (int i=1; i<=n; i++)
        {
            l1=0;
            l2=0;
            dfs1(i);
            if (l1==l2)
            {
                wyn+=l1*l2;
            }
            else
            {
                wek.push_back(make_pair(l1, l2));
            }

            l1=0;
            l2=0;
            dfs2(i);
            if (l1==l2)
            {
                wyn+=l1*l2;
            }
            else
            {
                wek.push_back(make_pair(l1, l2));
            }
        }
        if (wek.empty())
        {
            printf("%d\n", wyn);
            continue;
        }
        wek2.clear();
        sort(wek.begin(), wek.end());
        for (int i=0; i<wek.size(); i++)
        {
            if (!i || wek[i-1]!=wek[i])
            wek2.push_back(make_pair(wek[i], 0));
            wek2.back().second++;
        }
        vector <int> start;
        for (int i=0; i<wek2.size(); i++)
        start.push_back(0);

        mapa.clear();
        mapa[start]=-inf;

        rek(0);

        start.clear();
        for (int i=0; i<wek2.size(); i++)
        start.push_back(wek2[i].second);

        printf("%d\n", wyn+mapa[start]+inf);
    }
    return 0;
}
