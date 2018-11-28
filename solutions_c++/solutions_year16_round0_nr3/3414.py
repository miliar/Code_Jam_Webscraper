#include <iostream>
#include <cmath>
#include <vector>
#include <cstring>
#include <cstdio>
using namespace std;

const int N = 2000000;
int a[40];

void encode(int t) {
    a[0] = 1;
    for (int i = 30; i >= 1; i--) a[i] = t % 2, t /= 2;
    a[31] = 1;
}

int ispri(long long n) {
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return i;
    }
    return 0;
}

vector<long long> v;
vector<int> pri;

int main() {
    printf("Case #1:\n");
    int num = 0;
    for (int i = 0; i < (1 << 30); i++) {
        encode(i);
        long long t = 0, flag = 1, cnt = 0;
        for (int j = 0; j < 32; j++) t = t * 2 + a[j], cnt += a[j];
        if (t % 21 != 0 || cnt != 15) continue;
        t = 0;
        for (int j = 0; j < 32; j++) t = t * 3 + a[j];
        int now = ispri(t);
        if (now) {
            for (int j = 0; j < 32; j++) printf("%d", a[j]);
            printf(" 3 %d 3 3 5 3 3 7 3", now);
            puts("");
            num++;
        }
        if (num == 500) break;
    }
}
