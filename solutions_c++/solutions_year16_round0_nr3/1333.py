#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int nt[11] = {0, 0, 3, 2, 3, 2, 7, 2, 3, 2, 3};

int maxv = 0;
int bit[50];
int n, j;
int *value, *po;

int Nguyen_to(ll v) {
    if (v <= 3) return -1;
    if (v % 2 == 0) return 2;
    for(ll i = 3; i * i <= v; i += 2)
        if (v % i == 0) {
            return i;
        }
    return -1;
}

void Check(int* value) {
    for(int k = 2; k <= 10; ++k) {
        if (value[k] != 0) return;
    }
    --j;
    for(int i = n; i >= 1; --i) printf("%d", bit[i]);
    printf(" ");
    for(int i = 2; i <= 10; ++i) printf("%d ", nt[i]);
    printf("\n");
}

void Sinh(int len, int *value, int *p) {
    if (len > n) {
        if (bit[len - 1] == 1 && bit[1] == 1) Check(value);
        return;
    }
    if (j == 0) return;
    for(int i = 0; i <= 1; ++i) {
        if ((len == 1 || len == n) && i == 0) continue;
        if (j == 0) return;
        bit[len] = i;
        int * value1 = new int[11];
        int * p1 = new int[11];

        for(int k = 2; k <= 10; ++k) {
            value1[k] = value[k];
            p1[k] = p[k];
            value[k] = (value[k] + (ll)i * p[k]) % nt[k];
            p[k] = ((ll)p[k] * k) % nt[k];
        }
        Sinh(len + 1, value, p);
        for(int k = 2; k <= 10; ++k) {
            p[k] = p1[k];
            value[k] = value1[k];
        }
        delete[] value1;
        delete[] p1;
        if (j == 0) return;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests = 0;
    scanf("%d %d %d\n", &nTests, &n, &j);

    value = new int [11];
    po = new int [11];

    for(int i = 0; i < 11; ++i) value[i] = 0, po[i] = 1;

    printf("Case #1:\n");
    Sinh(1, value, po);

    delete[] value;
    delete[] po;
    return 0;
}
