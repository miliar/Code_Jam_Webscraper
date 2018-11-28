#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int c[10], sum = 0;
void add(long long x) {
    while (x > 0) {
        int k = x % 10;
        x /= 10;
        if (c[k] == 0) {
            c[k] = 1;
            sum++;
        }
    }
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("Al.out", "w", stdout);
    int T; long long n;
    cin >> T;
    for (int o = 1; o <= T; o++) {
        cin >> n;
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", o);
            continue;
        }
        memset(c, 0, sizeof c);
        sum = 0;
        long long check = 0;
        while (sum < 10) {
            check += n;
            add(check);
        }
        cout << "Case #" << o << ": " << check << endl;
    }
}
