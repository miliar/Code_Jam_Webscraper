#include <cstdio>
#include <math.h>
#include <cstring>
using namespace std;
int counter = 0;
void work() {
    printf("Case #%d: ", ++counter);
    unsigned int a, b, k;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &k);
    int pairs = 0;
    for (int i = 0; i < a; ++i) {
        for (int j = 0; j < b; ++j) {
            int c = i & j;
            // printf("a: %d, b: %d, c: %d\n", i, j, c);
            if( c < k) pairs++;
        }
    }
    printf("%d\n", pairs);
    return;
}

int main() {
    int t; scanf("%d", &t);
    while(t--) {
        work();
    }
    return 0;
}