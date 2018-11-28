#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))

int n, X;
int s[10000];
int a[10000];

int go(int m) {
    if (2 * m < n) {
        return 0;
    }

    int j = n - 1;
    for (int i = 0; i < m; ++i) {
        a[i] = s[j--];
    }

    j = 0;
    for (int i = 0; i < n - m; ++i) {
        while (j < m && a[j] + s[i] > X) {
            j++;
        }
        if (j >= m) {
            return 0;
        }
        j++;
    }
    return 1;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cs = 1; cs <= T; ++cs) {
        printf("Case #%d: ", cs);
        scanf("%d %d", &n, &X);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &s[i]);
        }
        sort(s, s + n);

        int low = 1, high = n;
        int mid;
        int sol = n;
        while (low <= high) {
            mid = (low + high) / 2;
            if (go(mid)) {
                sol = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        printf("%d\n", sol);
    }
    return 0;
}


