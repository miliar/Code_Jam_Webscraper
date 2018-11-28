#include <cstdio>
#include <iostream>

using namespace std;

string s[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

char d[] = "ZOWTUFXSGI";
const int N = 4000;
char str[N];
int ccount[128];

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        scanf("%s", str);
        memset(ccount, 0, sizeof(ccount));
        for (int j = 0; str[j]; ++j) {
            ++ccount[str[j]];
        }
        
        int ans[10] = {0};
        for (int p = 0; p < 2; ++p) {
            for (int j = p; j < 10; j += 2) {
                if (ccount[d[j]] > 0) {
                    int t = ccount[d[j]];
                    ans[j] = t;
                    for (int k = 0; k < s[j].length(); ++k) {
                        ccount[s[j][k]] -= t;
                    }
                }
            }
        }
        printf("Case #%d: ", i);
        for (int j = 0; j < 10; ++j) {
            for (int k = 0; k < ans[j]; ++k) {
                printf("%d", j);
            }
        }
        if (i + 1 <= T) {
            printf("\n");
        }
    }
    return 0;
}