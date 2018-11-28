#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <set>

using namespace std;

int N,M;
int tt, tw;
const int MOD = 1000000007;
char str[15][15];
int serv[5][15];
int cnt[5];

int prefixe(int i, int j, int k)
{
    int a = min(strlen(str[serv[i][j]]), strlen(str[serv[i][k]]));

    for(int p = 0; p < a; p++)
    {
        if(str[serv[i][j]][p] != str[serv[i][k]][p])
            return p;
    }
    return a;
}

int cree()
{
    int tt = 0;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < cnt[i]; j++)
        {
            int maxi = 0;
            for(int k = 0; k < j; k++)
            {
                maxi = max(maxi, prefixe(i,j,k));
            }
            tt += strlen(str[serv[i][j]]) - maxi;
        }
    }
    return tt;
}

void bourrin(int i)
{
    if(i == M)
    {
        int nb = 0;
        for(int j = 0; j < N; j++)
            if(cnt[j]==0)
                goto end;
        nb = cree()+N;
        if(nb > tt)
        {
            tt = nb;
            tw=1;
        }
        else if(nb == tt)
        {
            tw = (tw + 1)%MOD;
        }
        end:;
        return;
    }

    for(int j= 0; j < N; j++)
    {
        serv[j][cnt[j]++]=i;
        bourrin(i+1);
        cnt[j]--;
    }

}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        scanf("%d%d", &M, &N);
        tt=0, tw=0;

        for(int i = 0; i < M; i++)
        {
            scanf("%s", str[i]);
        }

        bourrin(0);

        printf("Case #%d: %d %d\n",t, tt, tw);
    }

    return 0;
}
