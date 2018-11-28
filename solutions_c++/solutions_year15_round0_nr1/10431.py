#include <utility>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

int n, friends, total, k;
char array[1234];

int main(int argc, char const *argv[]) {
    // freopen("ovation.in", "r", stdin);
    freopen("ovation.out", "w", stdout);
    scanf("%d\n", &n);
    for (int i = 1; i <= n; ++i)
    {
        total = 0;
        friends = 0;
        scanf("%d ", &k);
        for (int j = 0; j <= k; ++j)
        {
            scanf("%c", &array[j]);
        }
        total = array[0] - 48;
        for (int j = 1; j <= k; ++j)
        {
            int val = array[j] - 48;
            if (total < j && val != 0) {
                friends += j - total;
                total += friends;
            }
            total += val;
        }
        printf("Case #%d: %d", i, friends);
        if (i != n) printf("\n");
    }
    return 0;
}