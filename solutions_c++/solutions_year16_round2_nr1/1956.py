#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int MAXL = 2000 + 10;

char s[MAXL];

int num[300];
int cnt[100];
int ord[300];
int ch[300];
string g[300];

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w",stdout);
    int TestCase;
    scanf("%d", &TestCase);

    ord[1] = 0;
    ch[1] = 'Z';

    ord[2] = 2;
    ch[2] = 'W';

    ord[3] = 6;
    ch[3] = 'X';

    ord[4] = 8;
    ch[4] = 'G';

    ord[5] = 3;
    ch[5] = 'H';

    ord[6] = 4;
    ch[4] = 'R';

    ord[7] = 5;
    ch[7] = 'V';

    ord[8] = 7;
    ch[8] = 'S';

    ord[9] = 1;
    ch[9] = 'O';

    ord[10] = 9;
    ch[19] = 'N';

    g[0] = "ZERO";
    g[1] = "ONE";
    g[2] = "TWO";
    g[3] = "THREE";
    g[4] = "FOUR";
    g[5] = "FIVE";
    g[6] = "SIX";
    g[7] = "SEVEN";
    g[8] = "EIGHT";
    g[9] = "NINE";

    for (int nt = 1; nt <= TestCase; ++nt)
    {
        for (int i = 0; i < 10; ++i) cnt[i] = 0;
        memset(num, 0, sizeof(num));

        scanf("%s", s + 1);
        int len = strlen(s + 1);

        memset(num, 0, sizeof(num));
        for (int i = 1; i <= len; ++i)
            num[ s[i] ]++;

        for (int turn = 1; turn <= 10; ++turn)
        {
            int now = ord[turn];

            while (1)
            {
                for (int i = 0; i < g[now].length(); ++i)
                    --num[ g[now][i] ];

                bool flag = 0;
                for (int i = 'A'; i <= 'Z'; ++i)
                if (num[i] < 0) { flag = 1; break; }

                if(!flag) cnt[now]++;
                else
                {
                    for (int i = 0; i < g[now].length(); ++i)
                        ++num[ g[now][i] ];
                    break;
                }
            }
        }

        printf("Case #%d: ", nt);
        for (int i = 0; i < 10; ++i)
            for (int j = 1; j <= cnt[i]; ++j)
                printf("%d", i);
        printf("\n");
    }
    return 0;
}
