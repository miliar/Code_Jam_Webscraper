#include <iostream>
#include <algorithm>
#include <string.h>
#include <stdint.h>
#include <inttypes.h>
using namespace std;

int n, m;

int64_t getNum(int base, int *bits, int n) {
    int64_t ret = 0;
    for(int i = 0; i < n; i++) ret = ret * base + bits[i];
    return ret;
}

int64_t find(int64_t x) {
    for(int64_t i = 2; i * i < x; i++) {
        if(x % i == 0) return i;
    }
    return -1;
}

void dfs(int *bits, int n, int i, int64_t div[10]) {
    if(!m) return;
    if(i == n - 1) {
        for(int j = 2; j <= 10; j++) {
            int64_t num = getNum(j, bits, n);
            int64_t  d = find(num);
            if(d == -1) return;
            div[j] = d;
        }
        m--;
        for(int j = 0; j < n; j++)printf("%d", bits[j]);
        for(int j = 2; j <=10; j++)printf(" %lld", div[j]);
        printf("\n");
        return;
    }
    dfs(bits, n, i+1, div);
    bits[i] = 1;
    dfs(bits, n, i+1, div);
    bits[i] = 0;
}

int main() {
    int t;
    cin >> t;
    int c = 0;
    int bits[20];
    while(t--) {
        c++;
        printf("Case #%d:\n", c);
        cin >> n >> m;
        memset(bits, 0, sizeof(bits));
        bits[0] = 1;
        bits[n-1] = 1;
        int64_t div[10];
        dfs(bits, n, 1, div);
    }
    return 0;
}

