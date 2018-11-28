#include <iostream>
#include <cstring>
using namespace std;

int T, C;
char s[101];

int main() {
    scanf("%d", &T);
    C = 1;
    while (T--) {
        scanf("%s", s);
        int len = strlen(s);

        for (int i = len - 1; i >= 0; i++) {
            if (s[i] != '+') {
                s[i + 1] = '\0';
                break;
            }
        }

        len = strlen(s);
        int cnt = 0;
        for(int i = 1; i < len; i++) {
            if (s[i] == '-' && s[i-1] == '+') {
                cnt++;
            }
        }
        cnt *= 2;

        if (s[0] == '-') cnt++;

        printf("Case #%d: %d\n", C++, cnt);
    }
    return 0;
}
