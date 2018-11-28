#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int vol, nr, T, N, R, C, a[30][30], ap[30][30], cel[7][1009], Nr[7], v[7], X[40], Y[40], maxI[7][1009], maxJ[7][1009], dp[1009];
struct tetris
{
    int N;
    int a[7][7];
    tetris ()
    {
        N = 0;
        memset (a, 0, sizeof (a));
    }
}A[7][1009];

void fill_1 (int i, int j)
{
    if (ap[i][j] || a[i][j] == 0)
        return ;
    ap[i][j] = 1;
    fill_1 (i + 1, j);
    fill_1 (i - 1, j);
    fill_1 (i, j + 1);
    fill_1 (i, j - 1);
}

void fill_2 (int i, int j)
{
    if (ap[i][j] || a[i][j] || i == 0 || j == 0 || i > R || j > C)
        return ;
    vol ++;
    ap[i][j] = 1;
    fill_2 (i + 1, j);
    fill_2 (i - 1, j);
    fill_2 (i, j + 1);
    fill_2 (i, j - 1);
}

void back (int poz, int last)
{
    if (poz == N + 1)
    {
        for (int i=1; i<=N; i++)
            for (int j=1; j<=N; j++)
                ap[i][j] = 0, a[i][j] = 0;

        for (int i=1; i<=N; i++)
            a[X[v[i]]][Y[v[i]]] = 1;

        for (int i=1; i<=N; i++)
            for (int j=1; j<=N; j++)
                if (a[i][j])
                {
                    fill_1 (i, j);
                    i = N + 1;
                    break;
                }

        for (int i=1; i<=N; i++)
            for (int j=1; j<=N; j++)
                if (a[i][j] && ap[i][j] == 0)
                    return ;
        bool ok = 0;

        for (int i=1; i<=N; i++)
            if (a[i][1])
                ok = 1;

        if (ok == 0)
            return ;

        ok = 0;
        for (int j=1; j<=N; j++)
            if (a[1][j])
                ok = 1;

        if (ok == 0)
            return ;

        Nr[N] ++;
        A[N][Nr[N]].N = N;
        for (int i=1; i<=N; i++)
            for (int j=1; j<=N; j++)
                A[N][Nr[N]].a[i][j] = a[i][j];
        maxI[N][Nr[N]] = X[v[N]];
        for (int j=N; j>=1; j--)
            for (int i=1; i<=N; i++)
                if (a[i][j])
                {
                    maxJ[N][Nr[N]] = j;
                    j = 0;
                    break;
                }

        return ;
    }

    for (int i=last + 1; i<=nr; i++)
        v[poz] = i, back (poz + 1, i);
}

bool egal (tetris a, tetris b)
{
    for (int i=1; i<=a.N; i++)
        for (int j=1; j<=a.N; j++)
            if (a.a[i][j] != b.a[i][j])
                return 0;
    return 1;
}

tetris rotate_left (tetris a)
{
    tetris ans;
    ans.N = a.N;
    for (int i=1; i<=a.N; i++)
        for (int j=1; j<=a.N; j++)
            ans.a[i][j] = a.a[j][N - i + 1];
    return ans;
}

tetris translate (tetris a)
{
    int mini = a.N + 2, minj = a.N + 2;
    for (int i=1; i<=a.N; i++)
        for (int j=1; j<=a.N; j++)
            if (a.a[i][j])
            {
                if (i < mini)
                    mini = i;
                if (j < minj)
                    minj = j;
            }

    tetris ans;
    ans.N = a.N;
    for (int i=1; i<=a.N; i++)
        for (int j=1; j<=a.N; j++)
            if (a.a[i][j])
                ans.a[i - mini + 1][j - minj + 1] = 1;
    return ans;
}

void afis (tetris a)
{
    for (int i=1; i<=a.N; i++, printf ("\n"))
        for (int j=1; j<=a.N; j++)
            if (a.a[i][j]) printf ("#");
            else printf (".");
    printf ("\n\n");
}

int main ()
{
//freopen ("input", "r", stdin);
//freopen ("output", "w", stdout);

for (N = 1; N <= 6; N ++)
{
    ////generez toate onimoanele de ordin N cu tot cu intoarceri in matrici de N * N, considerand ca toate contine coltul stanga sus
    nr = 0;
    for (int i=1; i<=N; i++)
        for (int j=1; j<=N; j++)
            X[++nr] = i, Y[nr] = j;
    back (1, 0);
}

for (N = 1; N <= 6; N ++)
    for (int i=1; i<=Nr[N]; i++)
    {
        tetris a, b, c, d;
        a = A[N][i];
        b = translate (rotate_left (a));
        c = translate (rotate_left (b));
        d = translate (rotate_left (c));
        for (int j=1; j<=i; j++)
            if ( egal (A[N][j], a) || egal (A[N][j], b) || egal (A[N][j], c) || egal (A[N][j], d) )
            {
                cel[N][i] = j;
                break;
            }
    }

/*for (N = 4; N <= 4; N ++)
{
    printf ("pentru %d: %d combinatii\n", N, Nr[N]);
    for (int i=1; i<=Nr[N]; i++, printf ("\n\n"))
    {
        printf ("%d -> %d\n", i, cel[N][i]);
        for (int j=1; j<=N; j++, printf ("\n"))
            for (int k=1; k<=N; k++)
                printf ("%d", A[N][i].a[j][k]);
    }
}
return 0;*/

scanf ("%d", &T);
int test = 0;
while (test < T)
{
    printf ("Case #%d: ", ++test);
    scanf ("%d %d %d", &N, &R, &C);
    //printf ("%d %d %d  ", N, R, C);
    if (N >= 7 || (R * C) % N != 0 || N > max (R, C))
    {
        printf ("RICHARD\n");
        continue;
    }
    ////deja avem N <= 6 vom considera toate onimoanele de ordin N, pentru unul fixat vedem daca exista pozitie astfel incat componentele conexe in care imparte matricea sa fie conexe
    bool castig_ric = 0;
    for (int i = 1; i<=Nr[N]; i++)
    {
        int pot_cu_asta = 0;
        for (int a1 = 1; a1 + maxI[N][i] - 1 <= R; a1 ++)
            for (int b1 = 1; b1 + maxJ[N][i] - 1 <= C; b1 ++)
            {
                for (int j=1; j<=R; j++)
                    for (int k=1; k<=C; k++)
                        a[j][k] = A[N][i].a[j + a1 - 1][k + b1 - 1], ap[j][k] = 0;
                bool Ok = 1;
                for (int j=1; j<=R; j++)
                    for (int k=1; k<=C; k++)
                        if (a[j][k] == 0 && ap[j][k] == 0)
                        {
                            vol = 0;
                            fill_2 (j, k);
                            if (vol % N != 0)
                                Ok = 0;
                        }
                if (Ok)
                {
                    pot_cu_asta = 1;
                    a1 = R + 2;
                    break;
                }
            }

        if (pot_cu_asta == 0)
            dp[i] = 1;
        else
            dp[i] = 0;
    }

    /*for (int i=1; i<=N; i++)
    {
        printf ("%d -> %d\n", i, cel[N][i]);
        afis (A[N][i])
    }*/

    for (int i=1; i<=Nr[N]; i++)
    if (cel[N][i] == i)
    {
        int mini = dp[i];
        for (int j=i; j<=Nr[N]; j++)
            if (cel[N][j] == i && dp[j] < mini)
                mini = dp[j];

        if (mini == 1)
        {
            castig_ric = 1;
            break;
        }
    }

    if (castig_ric) printf ("RICHARD\n");
    else printf ("GABRIEL\n");
}

return 0;
}
