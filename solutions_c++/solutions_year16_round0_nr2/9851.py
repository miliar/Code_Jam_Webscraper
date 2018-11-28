#include <queue>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define FIN freopen("B-large.in", "r", stdin)
#define FOUT freopen("B-large.out", "w", stdout)

const int N = 102;

char s[N];

void reverse_and_xor(int m) {
    reverse(s, s + m);
    for(int i = 0; i < m; ++i) {
        s[i] = '+' + '-' - s[i];
    }
}

int main() {
    FIN;
    FOUT;
    int T, ncase = 0;
    scanf("%d", &T);
    while(T--) {
        scanf("%s", s);
        int n = strlen(s);
        int ans = 0;
        for(int i = n - 1; i >= 0; --i) {
            if(s[i] == '+') {
                continue;
            }
            else {
                int j = 0;
                while(j < n && s[j] == '+') {
                    ++j;
                }
                if(j == 0) {
                    reverse_and_xor(i + 1);
                    ans += 1;
                }
                else {
                    reverse_and_xor(j);
                    reverse_and_xor(i + 1);
                    ans += 2;
                }
            }
        }
        printf("Case #%d: %d\n", ++ncase, ans);
    }
    return 0;
}
