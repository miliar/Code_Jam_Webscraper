#include <bits/stdc++.h>

#define rep(i, j, k) for(int i = (int) j; i < (int) k; ++i)
#define ll long long
#define mp make_pair
using namespace std;

const int N = 2020;
char s[N];
int ltr[30];
int num[N], t;

int main()
{
#ifdef PIT
freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);
#endif // PIT
    int T, ic = 0;
    for(scanf("%d", &T); ic < T; ) {
        scanf("%s", s);
        int len = strlen(s);
        t = 0;
        memset(ltr, 0, sizeof ltr);
        for(int i = 0; i < len; ++i) {
            ltr[s[i] - 'A']++;
        }
        num[0] = ltr['Z' - 'A'];
        num[2] = ltr['W' - 'A'];
        num[4] = ltr['U' - 'A'];
        num[6] = ltr['X' - 'A'];
        num[8] = ltr['G' - 'A'];
        num[5] = ltr['F' - 'A'] - num[4];
        num[3] = ltr['H' - 'A'] - num[8];
        num[7] = ltr['S' - 'A'] - num[6];
        num[9] = ltr['I' - 'A'] - num[5] - num[6] - num[8];
        num[1] = ltr['N' - 'A'] - num[7] - 2 * num[9];

        printf("Case #%d: ", ++ic);
        for(int i = 0; i < 10; ++i) for(int j = 0; j < num[i]; ++j) printf("%d", i);
        puts("");
    }
    return 0;
}

