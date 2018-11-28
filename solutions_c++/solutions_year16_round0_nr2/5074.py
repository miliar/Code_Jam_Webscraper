#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int t;
    int c = 0;
    scanf("%d", &t);
    while (t--) {
        char *s = (char*) calloc(200, sizeof(char));
        scanf("%s", s);
        int l = strlen(s);
        int prev = -1;
        int ans = 0;
        for (int i = 0; i < l;) {
            char c = s[i];
            if (c == '+') {
                prev = i;
                i++;
            }
            else {
                if (prev != -1)
                    ans += 2;
                else
                    ans += 1;
                while (s[i] == '-')
                    i++;
            }
        }
        printf("Case #%d: %d\n", ++c, ans);
        free(s);
    }
    return 0;
}
