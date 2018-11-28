#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;
const int MAXN = 100000005;
vector<int> primer;
bool p[MAXN+5];
int c[100];
int ans[100];
int N, J;

int two(int x) {
    return 1 << x;
}
void init() {
    for (int i = 2; i < MAXN; i++) {
        if (!p[i]) primer.push_back(i);
        for (int j = i + i; j < MAXN; j += i)
            p[j] = true;
    }
}

bool check(long long k, int x) {
    for (int i = 0; i < primer.size(); i++) {
        long long t = primer[i];
        if (t * t > k) break;
        if (k % primer[i] == 0) {
            ans[x] = primer[i];
            return true;
        }
    }
    return false;
}

int main() {
    freopen("Csmall.out", "w", stdout);
    cout << "Case #1:" << endl;
    init();
   // cout << primer.size() << endl;
 //   for (int i = 0; i < primer.size(); i++)
   //     cout << primer[i] << " ";
    N = 16; J = 50;
    int sum = 0;
    for (int k = two(N-1); k < two(N); k++) {
        if (k % 2 == 0) continue;
        for (int i = 0; i < N; i++)
            c[i] = (k & (two(i))) > 0;
        bool ok = true;
        for (int b = 2; b <= 10; b++) {
            long long tmp = 0, base = 1;
            for (int i = 0; i < N; i++) {
                tmp += c[i] * base;
                base *= b;
            }
            if (!check(tmp, b)) {
                ok = false;
                break;
            }
        }
        if (ok) {
            for (int i = N - 1; i >= 0; i--)
                cout << c[i];
            for (int i = 2; i <= 10; i++)
                cout << " " << ans[i];
            cout << endl;
            J--;
            if (J == 0) break;
        }
    }
}
