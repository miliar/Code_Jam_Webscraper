#include <bits/stdc++.h>

using namespace std;

int R, C;
int A[100];
vector<int> adj[100];
bool seen[100];

int N(int x, int y)
{
    return (x*C+y)*4;
}

int E(int x, int y)
{
    return (x*C+y)*4+1;
}

int S(int x, int y)
{
    return (x*C+y)*4+2;
}

int W(int x, int y)
{
    return (x*C+y)*4+3;
}

int identify(int n)
{
    n--;
    if(n<C)
        return N(0, n);
    n-=C;
    if(n<R)
        return E(n, C-1);
    n-=R;
    if(n<C)
        return S(R-1, C-1-n);
    n-=C;
    return W(R-1-n, 0);
}

void connect(int u, int v)
{
    adj[u].push_back(v);
    adj[v].push_back(u);
}

void dfs(int u)
{
    seen[u]=true;
    for(auto& v: adj[u]) if(!seen[v])
        dfs(v);
}

void _main(int TEST)
{
    scanf("%d%d", &R, &C);
    for(int i=0; i<2*(R+C); i++)
        scanf("%d", A+i);
    for(int i=0; i<(1<<(R*C)); i++)
    {
        for(int j=0; j<100; j++)
            adj[j].clear(), seen[j]=false;
        for(int j=0; j<R; j++)
        {
            for(int k=0; k<C; k++)
            {
                if(k+1<C)
                    connect(E(j, k), W(j, k+1));
                if(j+1<R)
                    connect(S(j, k), N(j+1, k));
                int x=j*C+k;
                if((i>>x)&1) // /
                {
                    connect(N(j, k), W(j, k));
                    connect(S(j, k), E(j, k));
                }
                else
                {
                    connect(N(j, k), E(j, k));
                    connect(S(j, k), W(j, k));
                }
            }
        }
        bool ok=true;
        for(int i=0; i<2*(R+C); i+=2)
        {
            int x=identify(A[i]);
            int y=identify(A[i+1]);
            if(seen[x] || seen[y])
            {
                ok=false;
                break;
            }
            dfs(x);
            if(!seen[y])
            {
                ok=false;
                break;
            }
        }
        if(ok)
        {
            for(int j=0; j<R; j++)
            {
                for(int k=0; k<C; k++)
                {
                    int x=j*C+k;
                    if((i>>x)&1)
                        putchar('/');
                    else
                        putchar('\\');
                }
                printf("\n");
            }
            return;
        }
    }
    printf("IMPOSSIBLE\n");
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        printf("Case #%d:\n", i);
        _main(i);
    }
    return 0;
}
