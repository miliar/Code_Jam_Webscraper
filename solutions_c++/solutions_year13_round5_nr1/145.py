#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;

void solveTestCase() {
    ll B;
    int N;
    cin >> B >> N;
    vector<ll> x(N);
    for (int i = 0; i < N; ++i) {
        cin >> x[i];
    }
    while (x.size() < 37) x.push_back(0);
    x.push_back(ll(4e12));
    //x.push_back(ll(8e12));
    N = 37;
    sort(x.begin(), x.end());
    double result = 0.0;
    for (int width = 1; width <= 37; ++width) {
        ll l = 0, r = x[N - 1];
        while (r - l != 1) {
            ll m = (l + r) / 2;
            ll cnt = 0;
            ll cntW = 0;
            for (int i = 0; i < N; ++i) {
                if (i < width) {
                    cntW += max(0LL, m - 1 - x[i]);
                    cnt += max(0LL, m - 1 - x[i]);
                } else {
                    cnt += max(0LL, m - x[i]);
                }
            }
            if (cnt <= B) {
                result = max(result, cntW * 36.0 / width - cnt);
                l = m;
            } else
                r = m;
        }
    }
    printf("%.10lf\n", result);
}

int main(void) {
    int T;
    cin >> T;
    for (int testNo = 1; testNo <= T; ++testNo) {
        printf("Case #%d: ", testNo);
        solveTestCase();
    }
}
