#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>

using namespace std;

const double INF = 1e9;

int T, N, S;
double e[1001][1001];
int X[1001], Y[1001], Z[1001];

double dis[1001]; bool in[1001];

int sq(int x)
{
    return x*x;
}

void SPFA()
{
    queue<int> que;

    fill(dis, dis+N, INF);
    dis[0] = 0;
    que.push(0);
    in[0] = true;

    while( !que.empty() )
    {
        int p = que.front();
        que.pop();
        in[p] = false;

        for(int Ni = 0; Ni < N; Ni++)
            if( dis[Ni] > max(dis[p], e[p][Ni]) )
            {
                dis[Ni] = max(dis[p], e[p][Ni]);

                if( !in[Ni] )
                {
                    in[Ni] = true;
                    que.push(Ni);
                }
            }
    }
}

int main()
{
    freopen("C_small_in.txt", "r", stdin);
    freopen("C_small_out.txt", "w", stdout);

    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        scanf("%d %d", &N, &S);

        for(int Ni = 0; Ni < N; Ni++)
            scanf("%d %d %d %*d %*d %*d", &X[Ni], &Y[Ni], &Z[Ni]);

        for(int Ni = 0; Ni < N; Ni++)
            for(int Nj = 0; Nj < N; Nj++)
                e[Ni][Nj] = sqrt(sq(X[Ni]-X[Nj])+sq(Y[Ni]-Y[Nj])+sq(Z[Ni]-Z[Nj]) );

        SPFA();
        printf("Case #%d: %.8f\n", Ti, dis[1]);
    }
}
