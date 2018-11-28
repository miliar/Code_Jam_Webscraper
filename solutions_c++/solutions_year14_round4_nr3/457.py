#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

const int MAXN = 10*100*500+2;

int N, W, H, B, answer;
vector<int> G[MAXN], F[MAXN], Fb[MAXN], C[MAXN];
bool bad[100][500], mark[MAXN];

void add(int u, int v)
{
    Fb[u].push_back(F[v].size()); Fb[v].push_back(F[u].size());
    G[u].push_back(v); F[u].push_back(0); C[u].push_back(1);
    G[v].push_back(u); F[v].push_back(0); C[v].push_back(0);
}

bool dfs(int u)
{
    if (u == N-1) { ++answer; return true; }
    mark[u] = true;

    for (int e = 0; e < G[u].size(); ++e) {
        int v = G[u][e];

        if (F[u][e] < C[u][e] && !mark[v] && dfs(v)) {
            ++F[u][e]; --F[v][Fb[u][e]];
            //printf("?%d?", u);
            return true;
        }
    }

    return false;
}

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        printf("Case #%d: ", t+1);
        scanf("%d%d%d", &W, &H, &B);

        N = 2*W*H+2;
        for (int i = 0; i < N; ++i) {
            G[i].clear(); F[i].clear(); Fb[i].clear(); C[i].clear();
        }

        memset(bad, 0, sizeof(bad));

        for (int i = 0; i < B; ++i) {
            int X0, Y0, X1, Y1;
            scanf("%d%d%d%d", &X0, &Y0, &X1, &Y1);

            for (int X = X0; X <= X1; ++X)
                for (int Y = Y0; Y <= Y1; ++Y)
                    bad[X][Y] = true;
        }

        for (int X = 0; X < W; ++X)
            if (!bad[X][0]) add(0, W*H+X+1);

        for (int X = 0; X < W; ++X)
            if (!bad[X][H-1]) add(W*(H-1)+X+1, N-1);

        for (int X = 0; X < W; ++X)
            for (int Y = 0; Y < H; ++Y) {
                if (X+1 < W && !bad[X][Y] && !bad[X+1][Y]) add(W*Y+X+1, W*H+W*Y+X+2);
                if (Y+1 < H && !bad[X][Y] && !bad[X][Y+1]) add(W*Y+X+1, W*H+W*(Y+1)+X+1);
                if (X-1 >= 0 && !bad[X][Y] && !bad[X-1][Y]) add(W*Y+X+1, W*H+W*Y+X);
                if (Y-1 >= 0 && !bad[X][Y] && !bad[X][Y-1]) add(W*Y+X+1, W*H+W*(Y-1)+X+1);
            }

        for (int i = 0; i < W*H; ++i)
            add(W*H+i+1, i+1);

        answer = 0;
        while (true) {
            memset(mark, 0, sizeof(mark));
            if (!dfs(0)) break;
            //printf("\n");
        }
        printf("%d\n", answer);
    }

    return 0;
}
