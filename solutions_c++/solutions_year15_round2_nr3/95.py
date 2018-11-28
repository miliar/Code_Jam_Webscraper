#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

int nTest;
int n;
vector<pii> hiker;

int task1(vector<pii> hiker) {
    if (hiker.size() == 1) 
        return 0;
    else if (hiker.size() == 2) {
        sort(hiker.begin(), hiker.end());

        double t0 = double(360 - hiker[0].second) * hiker[0].first / 360 + hiker[0].first;
        double t1 = double(360 - hiker[1].second) * hiker[1].first / 360;

        if (t0 > t1)
            return 0;
        else
            return 1;
    } else {
        // Khong biet lam
        return -1;
    }
}

int main() {

    freopen("C-small-1-attempt0.in", "r", stdin);
    // froepen("C.out", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++) {

        scanf("%d", &n);
        hiker.clear();
        for (int i = 0; i < n; i++) {
            int d, h, m;
            scanf("%d%d%d", &d, &h, &m);

            for (int j = 0; j < h; j++)
                hiker.push_back({m + j, d});
        }
        printf("Case #%d: %d\n", test, task1(hiker));
        
    }

    return 0;
}
