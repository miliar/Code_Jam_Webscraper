#include <cstdio>
#include <cstring>

struct node
{
    int child[26];
};

const int MAXN = 20, MAXS = 20, MAXM = 20, MAXT = 400;
int nodeC[MAXN], theMax = 0, ways = 0;
int M, N;
node nodes[MAXN][MAXT];
char str[MAXM][MAXS];
int server[MAXM];

void solve(int now)
{
    if(now == M)
    {
        //simulation
        memset(nodeC, 0, sizeof(nodeC));

        //initialization
        for(int i = 0; i < N; i++)
        {
            for(int j = 0; j < 26; j++)
                nodes[i][0].child[j] = 0;
//            memset(nodes[i][0].child, 0, sizeof(nodes[i][0].child));
            ++nodeC[i];
        }        
        
        for(int i = 0; i < M; i++)
        {
            int len = strlen( str[i] );
            int s = server[i], now = 0;
            for(int j = 0; j < len; j++)
                if( nodes[s][ now ].child[ str[i][j] -'A' ] == 0 )
                {
                    nodes[s][ now ].child[ str[i][j] -'A' ] =  nodeC[s];
                    now = nodeC[s]++;
  //                  memset(nodes[s][now].child, 0, sizeof(nodes[s][now].child));
                    for(int k = 0; k < 26; k++)
                        nodes[s][now].child[k] = 0;
                }
                else now = nodes[s][now].child[ str[i][j]-'A'];
        }

        int tot = 0;
        for(int i = 0; i < N; i++)
        {
            if(nodeC[i] == 1) return ; //violating non-empty
            tot += nodeC[i];
        }
        
        /*printf("DEBUG %d\n", tot);
        for(int i = 0; i < M; i++)
            printf("%d ", server[i]);
        printf("\n");*/
        if(tot > theMax)
        {
            theMax = tot;
            ways = 1;
        }
        else if(tot == theMax)
            ++ways;
        return ;
    }

    for(int i = 0; i < N; i++)
    {
        server[now] = i;
        solve(now+1);
    }
}

int main()
{
    int TC;
    scanf("%d", &TC);

    for(int tc = 1; tc <= TC; tc++)
    {
        theMax = ways = 0;
        scanf("%d%d", &M, &N);

        for(int i = 0; i < M; i++)
            scanf("%s", str[i]);

        solve( 0 ); 
        printf("Case #%d: %d %d\n", tc, theMax, ways); 
    }

    return 0;
}
