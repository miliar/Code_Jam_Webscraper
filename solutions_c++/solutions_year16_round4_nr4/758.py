#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

int N;
char a[15][15];
char b[15][15];
vector <int> prm;
int f[15];
int mn;
int good;


void bck(int pas)
{
    if(!good)
        return;

    if(pas >= N)
        return;

    int ok = 0;
    for(int i = 1; i <= N; i++)
        if(!f[i] && b[ prm[pas] ][i] == 1)
        {
            f[i] = 1;
            bck(pas + 1);
            if(!good)
                return;
            f[i] = 0;
            ok = 1;
        }
    if(!ok)
    {
        good = 0;
        return;
    }
}

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; test++)
    {
        printf("Case #%d: ", test);

        scanf("%d\n", &N);
        int needmsk = 0;
        for(int i = 0; i < N; i++)
        {
            gets(a[i]);
            for(int j = 0; j < N; j++)
                if(a[i][j] == '1')
                    needmsk |= (1 << (i * N + j));
        }

        mn = N * N + 1;
        for(int msk = 0; msk < 1 << (N * N); msk++)
        {
            int cnt = 0;
            if( (msk & needmsk) != needmsk )    continue;
            for(int i = 0; i < N; i++)
                for(int j = 0; j < N; j++)
                {
                    b[i + 1][j + 1] = (msk >> (i * N + j)) & 1;
                    if(b[i + 1][j + 1] + '0' != a[i][j])
                        cnt++;
                }

            if(cnt > mn)    continue;

            good = 1;

            prm.clear();
            for(int i = 1; i <= N; i++)
                prm.push_back(i);

            do
            {
                if(!good)   break;
                memset(f, 0, sizeof(f));
                bck(0);
            }while( next_permutation(prm.begin(), prm.end()) && good);

            if(!good)   continue;

            mn = cnt;
        }

        printf("%d\n", mn);
    }

    return 0;
}
