#include <bits/stdc++.h>

using namespace std;

int N;
char S[5][5];
int ans, cnt;

bool dfs(int mask, int mask2)
{
    for(int i=0; i<N; i++) if((mask>>i)&1)
    {
        bool found=false;
        for(int j=0; j<N; j++) if(S[i][j]=='1' && !((mask2>>j)&1))
        {
            found=true;
            if(!dfs(mask&~(1<<i), mask2|(1<<j)))
                return false;
        }
        if(!found)
            return false;
    }
    return true;
}

void rec(int x, int y)
{
    if(x==N)
    {
        if(dfs((1<<N)-1, 0))
            ans=min(ans, cnt);
        return;
    }
    int nx=x, ny=y+1;
    if(ny==N)
        nx++, ny=0;
    if(S[x][y]=='0')
    {
        S[x][y]='1';
        cnt++;
        rec(nx, ny);
        cnt--;
        S[x][y]='0';
    }
    rec(nx, ny);
}

void _main(int TEST)
{
    scanf("%d", &N);
    for(int i=0; i<N; i++)
        scanf("%s", S[i]);
    ans=0x3f3f3f3f;
    cnt=0;
    rec(0, 0);
    printf("%d\n", ans);
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        printf("Case #%d: ", i);
        _main(i);
    }
    return 0;
}
