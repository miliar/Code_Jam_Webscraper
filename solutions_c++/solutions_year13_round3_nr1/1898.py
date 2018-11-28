#include <cstdio>
#include <cstring>

using namespace std;

bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

bool isConst(char c) {
    return !isVowel(c);
}

        char raw[1000000];
int main() {
    freopen("const.txt", "r", stdin);
    freopen("const2.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int test = 0; test < T; test++) {
        int n, len;
        scanf("%s %d", raw, &n);
        len = strlen(raw);

        int ans = 0;
        for (int start = 0; start < len; start++) {
            for (int end = start + 1; end < len + 1; end++) {
                int seqLen = 0, longestSeq = 0;
                for (int at = start; at < end; at++) {
                    if (isConst(raw[at])) {
                        seqLen++;
                    } else {
                        if (seqLen > longestSeq) {
                            longestSeq = seqLen;
                        }
                        seqLen = 0;
                    }
                }

                if (seqLen > longestSeq) {
                    longestSeq = seqLen;
                }

                if (longestSeq >= n) {
                    ans++;
                }
            }
        }

        printf("Case #%d: %d\n", test + 1, ans);
    }

    return 0;
}

