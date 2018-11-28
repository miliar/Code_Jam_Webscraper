#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
typedef long long LL;
vector<LL> v;

bool isPal(LL x) {
    vector<int> p;
    while (x > 0) {
        p.push_back(x % 10);
        x /= 10;
    }
    int k = 0;
    while (k < p.size() - k - 1) {
        if (p[k] != p[p.size() - 1 - k]) return false;
        k++;
    }
    return true;
}

void prep() {
    for (LL i = 1; i < 10000000; i++) {
        if (isPal(i) && isPal(i * i)) {
            v.push_back(i * i);
            //cout << i * i << endl;
        }
    }
//    printf("-- %d\n", v.size());
}

int solve() {
    LL a, b;
    scanf("%lld %lld", &a, &b);
    int ret = 0;
    for (int i = 0; i < v.size(); i++) {
        if (v[i] >= a && v[i] <= b) ret++;
    }
    return ret;
}

int main() {
    prep();
    int te;
    scanf("%d", &te);
    for (int i = 1; i <= te; i++) {
        int ret = solve();
        printf("Case #%d: %d\n", i, ret);
    }
}
