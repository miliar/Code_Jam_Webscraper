#include <stdio.h>

int t, tn;

int r, c;
char g[110][110];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int x[10010], y[10010];
bool safe[10010];
int anum;

int rcnt[110];
int ccnt[110];

bool able;
int ans;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("result.out", "w", stdout);
    
    int i, j, k, v;
    scanf("%d", &t);
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%d %d", &r, &c);
        for (i = 1; i <= r; i++) scanf("%s", g[i]+1);
        
        for (i = 1; i <= r; i++) rcnt[i] = 0;
        for (i = 1; i <= c; i++) ccnt[i] = 0;
        anum = 0;
        
        for (i = 1; i <= r; i++)
            for (j = 1; j <= c; j++)
            {
                if (g[i][j] == '.') continue;
                if (g[i][j] == '^') v = 0;
                if (g[i][j] == '>') v = 1;
                if (g[i][j] == 'v') v = 2;
                if (g[i][j] == '<') v = 3;
                
                rcnt[i]++;
                ccnt[j]++;
                
                x[anum] = i;
                y[anum] = j;
                for (k = 1; ; k++)
                {
                    if (i+dx[v]*k > r || i+dx[v]*k < 1 || j+dy[v]*k > c || j+dy[v]*k < 1)
                    {
                        safe[anum++] = false;
                        break;
                    }
                    if (g[i+dx[v]*k][j+dy[v]*k] == '.') continue;
                    safe[anum++] = true;
                    break;
                }
            }
        //printf("%d\n", anum);
        //for (i = 0; i < anum; i++) printf("%d %d %d\n", x[i], y[i], safe[i]);
        //for (i = 1; i <= r; i++) printf("%d ", rcnt[i]); puts("");
        //for (i = 1; i <= c; i++) printf("%d ", ccnt[i]); puts("");
        
        able = true;
        ans = 0;
        for (i = 0; i < anum; i++)
        {
            if (safe[i]) continue;
            if (rcnt[x[i]] == 1 && ccnt[y[i]] == 1)
            {
                able = false;
                break;
            }
            ans++;
        }
        
        printf("Case #%d: ", tn);
        if (able) printf("%d\n", ans);
        else puts("IMPOSSIBLE");
    }
}