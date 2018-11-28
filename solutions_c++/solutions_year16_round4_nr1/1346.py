#include <bits/stdc++.h>

using namespace std;

bool found;

char a[1<<12], s[1<<13];

int n, cr, cp, cs;

inline char getLoser(char winner) { return winner == 'S' ? 'P' : winner == 'R' ? 'S' : 'R'; }

inline char getWinner(char x, char y)
{
    if (x > y)
        swap(x, y);
    if (x == 'P')
        return y == 'R' ? 'P' : 'S';
    else if (x == 'R')
        return 'R';
}

bool better()
{    
    int from = 1<<n;
    for (int i = from; i < 1<<(n+1); ++i)
        if (a[i-from] > s[i])
            return true;
    return false;
}

void srt(int from, int to)
{
    if (from+1 == to)
        return;
    int mid = (to+from)>>1;
    srt(from, mid);
    srt(mid, to);
    for (int i = from; i < mid; ++i)
        if (s[i] > s[mid+i-from])
        {
            for (int j = from; j < mid; ++j)
                swap(s[j], s[mid+j-from]);
            break;
        }
}

void tryIt(char winner)
{
    s[1] = winner;
    for (int tour = 1; tour <= n; ++tour)
    {
        int from = 1<<tour;
        int to = 1<<(tour+1);
        for (int i = from; i < to; i += 2)
        {
            winner = s[i>>1];
            char loser = getLoser(winner);
            s[i] = min(loser, winner);
            s[i|1] = max(loser, winner);
        }
    }
    int nr, np, ns;
    nr = np = ns = 0;
    for (int i = 1<<n; i < 1<<(n+1); ++i)
    {
        if (s[i] == 'R')
            ++nr;
        else if (s[i] == 'P')
            ++np;
        else
            ++ns;
    }
    if (nr == cr && ns == cs && np == cp)
    {
        int from = 1<<n;
        int to = 1<<(n+1);
        srt(from, to);
        if (!found || better())
        {
            int from = 1<<n;
            for (int i = from; i < 1<<(n+1); ++i)
                a[i-from] = s[i];
            found = true;
        }
    }
}

int main()
{
    //freopen("sample1.in", "r", stdin);
    //freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n_tests;
    scanf("%d\n", &n_tests);

    for (int test_id = 1; test_id <= n_tests; ++test_id)
    {
        printf("Case #%d: ", test_id);

        scanf("%d %d %d %d\n", &n, &cr, &cp, &cs);

        found = false;

        tryIt('R');
        tryIt('P');
        tryIt('S');

        if (!found) 
            printf("IMPOSSIBLE");
        else
            for (int i = 0; i < 1<<n; ++i)
                printf("%c", a[i]);
        printf("\n");
    }

    return 0;
}
