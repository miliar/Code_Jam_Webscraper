#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

#define SIZE 17
#define UNSOLVED -1
#define INF 2147483647

int r, c, gNum, M[SIZE][1<<(SIZE-1)];

int collision_count(int bitmask, int pos)
{
    int col = 0;

    if(pos>=c && (bitmask&(1<<(pos-c))))
        col++;
    if(pos<gNum-c && (bitmask&(1<<(pos+c))))
        col++;
    if(pos%c>0 && (bitmask&(1<<(pos-1))))
        col++;
    if(pos%c<c-1 && (bitmask&(1<<(pos+1))))
        col++;

    return col;
}

int DP(int i, int j)
{
    if(!i)
        return 0;

    if(M[i][j]!=UNSOLVED)
        return M[i][j];

    int res, k;

    M[i][j] = INF;
    for(k = 0; k<gNum; ++k)
        if(!(j&(1<<k)))
        {
            res = DP(i-1, j|(1<<k));
            if(res<INF)
                M[i][j] = min(M[i][j], collision_count(j, k)+res);
        }

    return M[i][j];
}

int solve(int n)
{
    int b = 1<<(r*c), i;

    gNum = r*c;
    for(i = 1; i<=n; ++i)
        memset(&M[i][0], UNSOLVED, b*sizeof(int));

    return DP(n, 0);
}

int main()
{
    int test, t = 1, n;

    for(scanf("%d", &test); t<=test; ++t)
    {
        scanf("%d %d %d", &r, &c, &n);
        printf("Case #%d: %d\n", t, solve(n));
    }

    return 0;
}
