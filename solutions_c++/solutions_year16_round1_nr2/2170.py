#include <algorithm>
#include <bitset>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <limits>
#include <list>
#include <numeric>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

size_t heights[2501];

int main(int argc, const char *argv[]) {
    freopen("A_B.in", "r", stdin);
    freopen("A_B.out", "w", stdout);
    size_t t = 0;
    scanf("%zd", &t);
    for (size_t i = 1; i <= t; ++i) {
        printf("Case #%zd:", i);
        size_t n = 0;
        scanf("%zd", &n);
        memset(heights, 0, sizeof(heights));
        for (size_t j = 0; j < 2 * n - 1; ++j) {
            for (size_t k = 0; k < n; ++k) {
                size_t m = 0;
                scanf("%zd", &m);
                ++heights[m];
            }
        }
        size_t size = 0;
        for (size_t j = 1; j <= 2500 && size < n; ++j) {
            if (heights[j] % 2 == 1) {
                printf(" %zd", j);
                ++size;
            }
        }
        printf("\n");
    }
    return EXIT_SUCCESS;
}
