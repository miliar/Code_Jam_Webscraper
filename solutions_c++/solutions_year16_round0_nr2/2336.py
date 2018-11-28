#include<cstdio>
#include<queue>
#include<cstring>
#include<algorithm>

using namespace std;

int N, dp[1030], rev[1030][20], a[20];
char sir[20];
queue < int > cc;

int Move (int msk, int i)
{
    int lim = ((1 << i) - 1);
    return rev[msk & lim][i] + ((msk >> i) << i);
}

int main ()
{
freopen ("input", "r", stdin);
freopen ("output", "w", stdout);

int Tests;
scanf ("%d\n", &Tests);
for (int i=0; i<1024; i++)
    for (int j=1; j<=10; j++)
    {
        for (int k=0; k<10; k++)
            a[k + 1] = ((i & (1 << k)) > 0);
        reverse (a + 1, a + j + 1);
        for (int k=1; k<=j; k++)
            a[k] ^= 1;
        rev[i][j] = 0;
        for (int k=1; k<=10; k++)
            if (a[k]) rev[i][j] |= 1 << (k - 1);
    }
for (int test_id = 1; test_id <= Tests; test_id ++)
{
    printf ("Case #%d: ", test_id);
    gets (sir), N = strlen (sir);
    int msk = 0;
    for (int i=0; i<N; i++)
        if (sir[i] == '+') msk |= 1 << i;
    for (int i=0; i<1024; i++)
        dp[i] = -1;
    cc.push (msk), dp[msk] = 0;
    while (!cc.empty ())
    {
        int nod = cc.front ();
        cc.pop ();
        for (int i=1; i<=N; i++)
        {
            int vec = Move (nod, i);
            if (dp[vec] == -1) dp[vec] = dp[nod] + 1, cc.push (vec);
        }
    }
    printf ("%d\n", dp[(1 << N) - 1]);
}

return 0;
}
