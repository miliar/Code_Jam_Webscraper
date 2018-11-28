#include <set>
#include <map>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

#define MaxN 105

int N = 32, J = 500;

int output_str[MaxN];

int main() {
    freopen("output.txt", "w", stdout);
    printf("Case #1:\n");
    for (int i = 0; i < J; ++i) {
        int p = i * 2 + 1;
        for (int j = 0; j < N; j += 2) {
            output_str[j] = p % 2;
            p /= 2;
        }
        p = i * 2 + 1;
        for (int j = N - 1; j >= 0; j -= 2) {
            output_str[j] = p % 2;
            p /= 2;
        }
        for (int j = 0; j < N; ++j) {
            printf("%d", output_str[j]);
        }
        for (int j = 2; j <= 10; ++j) {
            if (j % 2 == 0)
                printf(" %d", j + 1);
            else
                printf(" 2");
        }
        puts("");
    }
    return 0;
}
