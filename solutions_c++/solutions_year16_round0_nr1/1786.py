#include <set>
#include <cstdio>
#include <algorithm>

using namespace std;

int T, n;
set <int> s;

int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        printf("Case #%d: ", t);
        if (n == 0) {
            printf("INSOMNIA\n");
        } else {
            int x = -1;
            for (int i = 1;; i++) {
                int y = i * n;
                while (y > 0) {
                    s.insert(y % 10);
                    y /= 10;
                }
                if (s.size() == 10) {
                    x = i;
                    break;
                }
            }
            printf("%d\n", x * n);
        }
        s.clear();
    }

    return 0;

}
