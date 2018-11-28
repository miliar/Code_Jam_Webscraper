#include <fstream>
#include <cstring>

#define maxn 110

using namespace std;

ifstream fin("test.in");
ofstream fout("test.out");

int n,m,x,y;
char s[maxn][maxn];
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
int destx[maxn][maxn], desty[maxn][maxn], viz[maxn][maxn], pred[maxn][maxn];
int d[300];

bool valid (int i, int j)
{
    return (1 <= i && i <= n && 1 <= j && j <= m);
}

int solve()
{
    d['^'] = 0;
    d['v'] = 1;
    d['<'] = 2;
    d['>'] = 3;

    fin >> n >> m;

    for (int i = 1; i <= n; ++i)
    {
        fin >> s[i] + 1;
    }

    int ans = 0;

    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= m; ++j)
        {
            if (s[i][j] == '.')
                continue;

            int dir = d[s[i][j]];

            int ii, jj;

            for (ii = i+dx[dir], jj = j+dy[dir]; valid(ii,jj) && s[ii][jj] == '.'; ii += dx[dir], jj += dy[dir]);

            if (!valid(ii,jj))
            {
                bool ok = 0;

                for (int k = 0; k < 4; ++k)
                {
                    int dir = k;
                    int ii,jj;
                    for (ii = i+dx[dir], jj = j+dy[dir]; valid(ii,jj) && s[ii][jj] == '.'; ii += dx[dir], jj += dy[dir]);

                    if (valid(ii,jj))
                    {
                        ok = 1;
                        break;
                    }
                }

                if(!ok)
                    return -1;
                ++ans;
            }
        }
    }

    return ans;
}

void reset()
{
    memset(viz,0,sizeof(viz));
    memset(pred,0,sizeof(pred));
}

int main()
{
    int test;

    fin >> test;

    for (int k = 1; k <= test; ++k)
    {
        reset();
        int answer = solve();
        fout << "Case #" << k << ": ";
        if (answer == -1)
            fout << "IMPOSSIBLE";
        else fout << answer;
        fout << "\n";
    }
}
