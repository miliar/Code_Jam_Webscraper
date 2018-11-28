#include<stdio.h>
#include<vector>
#include<cstring>
using namespace std;
#define nmax 15
#define lgmax 15
struct nod{int ncuv, npref, v['Z'-'A'+2];
    void init()
    {
        for (char c='A';c<='Z';c++)
            v[c]=0;
    }
};

bool ok;
char s[nmax][lgmax];
nod ng;
vector <nod> tr[nmax];
int t, ii, i, n, m, ls, p1, pt, reza, rez, nrez, nr[nmax], sol[nmax];

void adauga(int nod, int poz)
{
    if (poz==ls)
        tr[pt][nod].ncuv++;
    else
    {
        if (tr[pt][nod].v[s[p1][poz]-'A']==0)
        {
            tr[pt].push_back(ng);
            tr[pt][nod].v[s[p1][poz]-'A']=tr[pt].size()-1;

        }
        adauga(tr[pt][nod].v[s[p1][poz]-'A'],poz+1);
    }
    tr[pt][nod].npref++;
}

void calculare()
{
    ok=1;
    for (i=1;i<=n;i++)
    {
        if (nr[i]==0)
            ok=0;
    }
    if (ok)
    {
        for (i=1;i<=n;i++)
            tr[i].push_back(ng);
        for (i=1;i<=m;i++)
        {
            p1=i;   pt=sol[i];
            ls=strlen(s[p1]);
            adauga(0,0);
        }
        reza=0;
        for (i=1;i<=n;i++)
        {
            reza+=tr[i].size();
            tr[i].clear();
        }
        if (reza>rez)
        {
            rez=reza;
            nrez=0;
        }
        if (reza==rez)
            nrez++;
    }
}

void gen(int poz)
{
    if (poz==m+1)
        calculare();
    else
    {
        for (int x=1;x<=n;x++)
        {
            nr[x]++;
            sol[poz]=x;
            gen(poz+1);
            nr[x]--;
        }
    }
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%ld",&t);
    for (ii=1;ii<=t;ii++)
    {
        scanf("%ld %ld",&m,&n);
        for (i=1;i<=m;i++)
            scanf("%s",s[i]);
        rez=-1;
        gen(1);
        printf("Case #%ld: %ld %ld\n",ii,rez,nrez);
    }
    return 0;
}
