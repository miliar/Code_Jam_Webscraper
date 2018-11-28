#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
int q[20];
bool check(long long a) {
    int k = 0;
    while (a > 0) {
        q[++k] = a % 10;
        a = a / 10;
    }
    for (int i = 1; i <= k / 2; ++i) 
    if (q[i] != q[k - i + 1]) return false;
    return true;
}

vector<long long> v;
int main() {
    //freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (long long i = 1; i <= 10000000; ++i) {
        if (check(i) && check(i * i)) v.push_back(i * i);
    }
  //  for (int i = 0; i < v.size(); ++i) cout << v[i] << endl;
    long long l, r;
    for (int t = 1; t <= test; ++t) {
        cin >> l >> r;
        int ans = 0;
        //int ans = lower_bound(v.begin(), v.end(), r + 1) - lower_bound(v.begin(), v.end(), l);
        for (int i = 0; i < v.size(); ++i)
            if (v[i] >= l && v[i] <= r) ++ans;
        cout << "Case #" << t << ": " << ans << endl;
    } 
}
