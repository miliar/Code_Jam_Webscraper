#include <cstdio>
#include <cstring>

using namespace std;

int main(void)
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    int T, cnt[30], ans[15], len;
    char S[2005];

    scanf("%d", &T);
    for(int x = 1; x <= T; ++x) {
        memset(cnt, 0, sizeof(cnt));
        memset(ans, 0, sizeof(ans));
        scanf("%s", S);
        len = strlen(S);

        for(int i = 0; i < len; ++i) {
            ++cnt[S[i]-'A'];
        }

        //ZERO
        ans[0] += cnt['Z'-'A'];
        cnt['E'-'A'] -= cnt['Z'-'A']; cnt['R'-'A'] -= cnt['Z'-'A']; cnt['O'-'A'] -= cnt['Z'-'A'];

        //TWO
        ans[2] += cnt['W'-'A'];
        cnt['T'-'A'] -= cnt['W'-'A']; cnt['O'-'A'] -= cnt['W'-'A'];

        //FOUR
        ans[4] += cnt['U'-'A'];
        cnt['F'-'A'] -= cnt['U'-'A']; cnt['O'-'A'] -= cnt['U'-'A']; cnt['R'-'A'] -= cnt['U'-'A'];

        //SIX
        ans[6] += cnt['X'-'A'];
        cnt['S'-'A'] -= cnt['X'-'A']; cnt['I'-'A'] -= cnt['X'-'A'];

        //EIGHT
        ans[8] += cnt['G'-'A'];
        cnt['E'-'A'] -= cnt['G'-'A']; cnt['I'-'A'] -= cnt['G'-'A']; cnt['H'-'A'] -= cnt['G'-'A']; cnt['T'-'A'] -= cnt['G'-'A'];

        //SEVEN
        ans[7] += cnt['S'-'A'];
        cnt['E'-'A'] -= cnt['S'-'A']; cnt['V'-'A'] -= cnt['S'-'A']; cnt['E'-'A'] -= cnt['S'-'A']; cnt['N'-'A'] -= cnt['S'-'A'];

        //FIVE
        ans[5] += cnt['F'-'A'];
        cnt['I'-'A'] -= cnt['F'-'A']; cnt['V'-'A'] -= cnt['F'-'A']; cnt['E'-'A'] -= cnt['F'-'A'];

        //NINE
        ans[9] += cnt['I'-'A'];
        cnt['N'-'A'] -= cnt['I'-'A']; cnt['N'-'A'] -= cnt['I'-'A']; cnt['E'-'A'] -= cnt['I'-'A'];

        //ONE
        ans[1] += cnt['O'-'A'];
        cnt['N'-'A'] -= cnt['O'-'A']; cnt['E'-'A'] -= cnt['O'-'A'];

        //THREE
        ans[3] += cnt['T'-'A'];
        cnt['H'-'A'] -= cnt['T'-'A']; cnt['R'-'A'] -= cnt['T'-'A']; cnt['E'-'A'] -= cnt['T'-'A']; cnt['E'-'A'] -= cnt['T'-'A'];


        printf("Case #%d: ", x);
        for(int i = 0; i < 10; ++i) {
            while(ans[i] > 0) {
                printf("%d", i);
                --ans[i];
            }
        }
        printf("\n");

    }

    return 0;
}
