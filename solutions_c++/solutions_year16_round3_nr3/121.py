#include <cstdio>

using namespace std;

#define maxn 5
#define maxl 1000010

int t, n, m;
int jp[maxn][maxn], js[maxn][maxn], ps[maxn][maxn];
int e[maxl], p[maxl], s[maxl];
int conf[maxl], csol[maxl];
int sol;

void back(int nod, int tot)
{
    if(nod==n)
    {
        if(tot>sol)
        {
            sol=tot;
            for(int i=0; i<n; ++i)
                csol[i]=conf[i];
        }
        return;
    }

    int a=e[nod], b=p[nod], c=s[nod];

    conf[nod]=0;
    back(nod+1, tot);

    if(jp[a][b]<m && js[a][c]<m && ps[b][c]<m)
    {
        ++jp[a][b];
        ++js[a][c];
        ++ps[b][c];

        conf[nod]=1;
        back(nod+1, tot+1);

        --jp[a][b];
        --js[a][c];
        --ps[b][c];
    }
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("data.out", "w", stdout);

    scanf("%d", &t);
    for(int test=1; test<=t; ++test)
    {
        int a, b, c;
        scanf("%d%d%d%d", &a, &b, &c, &m);

        n=0;
        for(int i=1; i<=a; ++i)
            for(int j=1; j<=b; ++j)
                for(int k=1; k<=c; ++k)
                {
                    e[n]=i;
                    p[n]=j;
                    s[n]=k;
                    ++n;
                }

        sol=0;
        back(0, 0);

        printf("Case #%d: %d\n", test, sol);

        for(int i=0; i<n; ++i)
        {
            if(csol[i])
                printf("%d %d %d\n", e[i], p[i], s[i]);
        }
    }

    return 0;
}
