#include <stdio.h>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <cstring>


unsigned keyboard[40];
unsigned pattern[200];
double dp[110][110];
unsigned prefix_func[200];

int main()
{
    unsigned num_test = 0;
    scanf("%u", &num_test);
    for (unsigned T = 0; T < num_test; ++T) {
        unsigned K, L, S;
        scanf("%u %u %u\n", &K, &L, &S);
        memset(keyboard, 0, sizeof(keyboard));
        for (unsigned i = 0; i < K; ++i) {
            char chr;
            scanf("%c", &chr);
            ++keyboard[chr - 'A'];
        }
        scanf("\n");
        for (unsigned i = 0; i < L; ++i) {
            char chr;
            scanf("%c", &chr);
            pattern[i] = chr - 'A';
        }
        for (unsigned str_pos = 0; str_pos < S; ++str_pos) {
            for (unsigned pref = 0; pref < L && pref <= str_pos; ++pref) {
                const double next_chr_prob =  double(keyboard[pattern[pref]]) / K;
            //    printf("%u %u\n", pattern[pref], keyboard[pattern[pref]]);
                if (pref == 0) {
                    dp[str_pos][pref] = next_chr_prob;
                }
                else {
                    dp[str_pos][pref] = dp[str_pos - 1][pref - 1] * next_chr_prob;
                }
            //    printf("dp[%u][%u] = %lf\n", str_pos, pref, dp[str_pos][pref]);
            }
        }
        double expected = 0;
        for (unsigned i = 0; i < S; ++i) {
            expected += dp[i][L - 1];
        }
        memset(prefix_func, 0, sizeof(prefix_func));
        for (unsigned i = 1; i < L; ++i) {
            unsigned j = prefix_func[i - 1];
            while (j > 0 && pattern[i] != pattern[j]) {
                j = prefix_func[j - 1];
            }
            if (pattern[i] == pattern[j]) {
                ++j;
            }
            prefix_func[i] = j;
        }
        bool can_type = true;
        for (unsigned i = 0; i < L; ++i) {
            can_type = can_type && (keyboard[pattern[i]] != 0);
        }
        unsigned max_answer = 0;
        if (can_type) {
            unsigned pos = L - 1;
            while (pos < S) {
                ++max_answer;
                pos += L - prefix_func[L - 1];
            }
        }
        double answer = max_answer - expected;
        printf("Case #%u: %.7lf\n", T + 1, answer);
    }
    return 0;
}
