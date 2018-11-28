#include <cstdio>
#include <queue>
#include <cstring>
using namespace std;

const int maxN = 1 << 10;

int dist[maxN];
bool vis[maxN];

queue <int> Q;

int main()
{
    int tests;
    scanf ("%d", &tests);

    for (int t=1; t<=tests; t++)
    {
        char in[11];
        scanf ("%s", in);

        unsigned int s = strlen(in), target = (1 << s) - 1, source = 0;

        for (int i=0; i<s; i++)
        {
            if (in[i] == '+')
                source |= (1 << i);
        }

        dist[source] = 0;
        vis[source] = 1;
        Q.push(source);

        while (!Q.empty())
        {
            unsigned int v = Q.front(), inv = 0;
            Q.pop();

            for (int i=1; i<=s; i++)
            {
                inv = inv * 2 + ((v & (1 << (i - 1))) == 0);
                unsigned int u = (v ^ (v % (1 << i))) | inv;

                if (vis[u])
                    continue;

                vis[u] = 1;
                dist[u] = dist[v] + 1;
                Q.push(u);
            }
        }

        printf("Case #%d: %d\n", t, dist[target]);

        for (int i=0; i<=target; i++)
            vis[i] = 0;
    }

    return 0;
}
