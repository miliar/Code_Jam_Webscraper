#include <cstdio>
#include <cstring>
int n, m;
int h[150][150];
bool cut[150][150][2];

void init()
{
    memset(cut, 1, sizeof(cut));
    scanf("%d%d", &n, &m);
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            scanf("%d", &h[i][j]);
}

bool solve()
{
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            for(int k=0; k<n; k++)
                if(h[k][j] > h[i][j]) cut[i][j][0] = 0;
            for(int k=0; k<m; k++)
                if(h[i][k] > h[i][j]) cut[i][j][1] = 0;

            if(!cut[i][j][0] && !cut[i][j][1])return false;
        }
    }
    return true;
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int cas=0; cas<T; cas++){
        printf("Case #%d: ", 1+cas);
        init();
        puts(solve()?("YES"):("NO"));
    }
    return 0;
}
