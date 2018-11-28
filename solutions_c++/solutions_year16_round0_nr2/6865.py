#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAXL = 110;
char s[MAXL];

void reverse(char* a, int l) {
    for (int i = 0; i <= l; i++) {
        if (s[i] == '-') s[i] = '+';
        else s[i] = '-';
    }
}

int main() {
    int t;
    scanf("%d\n", &t);
    for (int k = 1; k <= t; k++) {
        scanf("%s\n", s);
        int l = strlen(s);
        int ans = 0;
        for (int i = l - 1; i >= 0; i--) {
            if (s[i] != '+') {
                ans++;
                reverse(s, i);
            }
        }
        printf("Case #%d: %d\n", k, ans);
    }
    return 0;
}
