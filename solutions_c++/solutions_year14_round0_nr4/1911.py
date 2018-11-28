#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<double> conA, conB;
deque<double> dqA, dqB;

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    int T, n;
    double d;
    scanf("%d", &T);

    for (int times = 0; times < T; times++) {
        conA = conB = vector<double>();
        scanf("%d", &n);

        for (int i = 0; i < n; i++) {
            scanf("%lf", &d);
            conA.push_back(d);
        }
        for (int i = 0; i < n; i++) {
            scanf("%lf", &d);
            conB.push_back(d);
        }

        sort(conA.begin(), conA.end());
        sort(conB.begin(), conB.end());

        int ds = 0;
        int ws = 0;

        for (int i = 0; i < n; i++) {
            dqA.push_back(conA[i]);
            dqB.push_back(conB[i]);
        }
        while (dqA.size()) {
            if (dqA.back() < dqB.back()) {
                dqA.pop_front();
                dqB.pop_back();
            }
            else {
                dqA.pop_back();
                dqB.pop_back();
                ds++;
            }
        }

        for (int i = 0; i < n; i++) {
            dqA.push_back(conA[i]);
            dqB.push_back(conB[i]);
        }
        while (dqA.size()) {
            if (dqA.back() > dqB.back()) {
                dqA.pop_back();
                dqB.pop_front();
                ws++;
            }
            else {
                dqA.pop_back();
                dqB.pop_back();
            }
        }

        printf("Case #%d: %d %d\n", times + 1, ds, ws);
    }
}
