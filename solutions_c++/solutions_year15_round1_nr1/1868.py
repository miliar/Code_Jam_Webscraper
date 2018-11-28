/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2015
 * Round 1A, Problem A
 */
#include <cstdio>
#include <algorithm>

using namespace std;

int shrooms[1010];

int main() {
    int t;
    scanf("%d", &t);
    for (int c = 1; c <= t; ++c) {
        int n, x, z;
        x = z = 0;
        int maxDiff = 0;
        scanf("%d", &n);
        
        for (int i = 0; i < n; ++i) {
            scanf("%d", &shrooms[i]);
            if (i > 0) {
                maxDiff = max(shrooms[i - 1] - shrooms[i], maxDiff);
            }
            int negDiff = shrooms[i - 1] - shrooms[i];
            x += (negDiff > 0) ? negDiff : 0;
        }
        
        for (int i = 0; i < n - 1; ++i) {
            z += min(maxDiff, shrooms[i]);
        }
        
        printf("Case #%d: %d %d\n", c, x, z);
    }
    return 0;
}