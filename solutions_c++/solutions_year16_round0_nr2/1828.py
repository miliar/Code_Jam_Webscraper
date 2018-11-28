#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 2000;

int T;
char s[N];

int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%s", s);
        int n = strlen(s);
        int cnt = 0;
        for (int i = 0; i < n;) {
            int j = i;
            while (j < n && s[i] == s[j]) {
                j++;
            }
            cnt++;
            i = j;
        }
        if (s[n - 1] == '+') {
            cnt--;
        }
        printf("Case #%d: %d\n", t, max(0, cnt));
    }

    return 0;

}
