#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
using namespace std;

const int MAXR = 5;
int ans[MAXR * MAXR];
bool was[MAXR * MAXR];
const int EMPTY = 0;
const int MINE = 1;
const int CLICK = 2;

int r, c, m;
#define MAT(m,i,j) (m[(i) * c + (j)])

void dfs(int i0, int j0)
{
    int i, j, di, dj;
    MAT(was,i0,j0) = true;
    bool was_mn = false;
    for(di = -1; di <= 1; ++di)
        for(dj = -1; dj <= 1; ++dj)
        {
            i = i0 + di;
            j = j0 + dj;
            if(0 <= i && i < r && 0 <= j && j < c && MAT(ans,i,j) == MINE)
                was_mn = true;
        }
    if(!was_mn)
        for(di = -1; di <= 1; ++di)
            for(dj = -1; dj <= 1; ++dj)
            {
                i = i0 + di;
                j = j0 + dj;
                if(0 <= i && i < r && 0 <= j && j < c &&
                    MAT(ans, i, j) != MINE && !MAT(was, i, j))
                    dfs(i, j);
            }
}

bool ok()
{
    memset(was, 0, sizeof(was));
    dfs(0, 0);
    int i, j;
    int was_cnt = 0;
    for(i = 0; i < r; ++i)
        for(j = 0; j < c; ++j)
            was_cnt += MAT(was, i, j);
    return was_cnt == r * c - m;
}

bool BF(int pos, int placed)
{
    if(pos == r * c)
        return ok();
    if(r * c - pos > m - placed)
    {
        ans[pos] = EMPTY;
        if(BF(pos + 1, placed))
            return true;
    }
    if(placed < m)
    {
        ans[pos] = MINE;
        if(BF(pos + 1, placed + 1))
            return true;
    }
    return false;
}

void test(int testNum)
{
    int i, j;
    
    scanf("%d%d%d", &r, &c, &m);
    printf("Case #%d:\n", testNum);
    
    ans[0] = CLICK;
    if(BF(1,0))
        for(i = 0; i < r; ++i)
        {
            for(j = 0; j < c; ++j)
                switch(MAT(ans, i, j))
                {
                    case CLICK:
                        putchar('c');
                        break;
                    case EMPTY:
                        putchar('.');
                        break;
                    case MINE:
                        putchar('*');
                        break;
                    default:
                        putchar('?');
                        break;
                }
            putchar('\n');
        }
    else
        puts("Impossible");
}

int main()
{
    assert(freopen("/Users/seriy/Google Code Jam 2014/Qualification Round/C/C/C-small-attempt1.in", "r", stdin) != NULL);
    assert(freopen("/Users/seriy/Google Code Jam 2014/Qualification Round/C/C/output.txt", "w", stdout) != NULL);
    int t, testn;
    scanf("%d", &testn);
    for(t = 1; t <= testn; ++t)
        test(t);
    return 0;
}

