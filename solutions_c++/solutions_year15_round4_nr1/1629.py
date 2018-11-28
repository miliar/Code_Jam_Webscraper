#include <cstdio>
#include <map>

using namespace std;
char mat[105][105];
int N,M;
map<char,int> ctoi;

const int dx[5]={0,-1,0,1,0},
          dy[5]={0,0,1,0,-1};

void Read()
{
    scanf("%d%d",&N,&M);
    for(int i = 1; i <= N; ++i)
        scanf("%s",mat[i] + 1);
}

int verif(int x,int y,char c)
{
    int d = ctoi[c];

    x += dx[d];
    y += dy[d];

    while(1 <= x && x <= N && 1 <= y && y <= M && mat[x][y] == '.')
    {
        x += dx[d];
        y += dy[d];
    }

    if(1 <= x && x <= N && 1 <= y && y <= M)
        return 1;
    return 0;
}

int main()
{
    freopen("pegman.in","r",stdin);
    freopen("pegman.out","w",stdout);

    ctoi['^'] = 1;
    ctoi['>'] = 2;
    ctoi['v'] = 3;
    ctoi['<'] = 4;

    int T;scanf("%d",&T);
    for(int tst = 1; tst <= T; ++tst){
        Read();
        int steps = 0,bad = 0;
        for(int i = 1; i <= N; ++i)
            for(int j = 1; j <= M; ++j)
                if(mat[i][j] != '.')
                {
                    int ok,ok2 = 0;
                    ok = verif(i,j,mat[i][j]);
                    if(ok == 1)
                        continue;
                    ok2 |= verif(i,j,'^');
                    ok2 |= verif(i,j,'>');
                    ok2 |= verif(i,j,'v');
                    ok2 |= verif(i,j,'<');
                    if(ok2)
                        ++steps;
                    else
                    {
                        bad = 1;
                        i = N + 1;
                        j = M + 1;
                    }
                }
        if(bad)
            printf("Case #%d: IMPOSSIBLE\n",tst);
        else
            printf("Case #%d: %d\n",tst,steps);

    }
    return 0;
}
