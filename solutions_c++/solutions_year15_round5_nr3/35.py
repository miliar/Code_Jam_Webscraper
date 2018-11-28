#include <iostream>
#include <string>
#include <array>
#include <cstring>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <unordered_map>
#include <iomanip>
#include <sstream>
#include <limits>
#include <float.h>

using namespace std;

int t, n;
double y;
double p[30];
double s[30];

double EPSILON = 1e-9;

bool same(double a, double b)
{
    return fabs(a - b) < EPSILON;
}

double abs(double a, double b) {
    return (a - b < 0 ? b - a : a - b);
}

bool caught[30];

double curMin = DBL_MAX;;
void getMin(int dir, double curPos, int depth, double cur) {
    if (cur >= curMin) {
        return;
    }
    double ptmp[26], cbefore[26];
    memcpy(ptmp, p, sizeof(ptmp));
    memcpy(cbefore, caught, sizeof(cbefore));

    double minTmp = DBL_MAX;
    int caughtIndex = -1;
    for (int i = 0; i < n; i++) {
        if (caught[i]) continue;
        double tmp = abs(p[i] - curPos) / (y - s[i]);
        // cout << i << " " << tmp << " " << p[i] << " " << curPos << " " << y << " " << s[i] << endl;
        if (same(tmp, 0)) {
            caught[i] = true;
        } else if ((p[i] - curPos) * dir < 0) {
            continue;
        }
        if (!caught[i] && tmp > 0 && tmp < minTmp) {
            minTmp = tmp;
            caughtIndex = i;
        }
    }
    // cout << dir << " " << minTmp << " " << depth << endl;

    if (caughtIndex != -1) {
        caught[caughtIndex] = true;
        for (int i = 0; i < n; i++) {
            if (caught[i]) continue;
            if (curPos > p[i]) {
                p[i] = p[i] - s[i] * minTmp;
            } else {
                p[i] = p[i] + s[i] * minTmp;
            }
        }
        getMin(1, curPos + y * minTmp * dir, depth + 1, minTmp + cur);
        ;
        getMin(-1, curPos + y * minTmp * dir, depth + 1, minTmp + cur);
        memcpy(p, ptmp, sizeof(p));
        memcpy(caught, cbefore, sizeof(caught));
        return;
    } else {
        for (int i = 0; i < n; i++) {
            if (!caught[i]) {
                memcpy(p, ptmp, sizeof(p));
                memcpy(caught, cbefore, sizeof(caught));
                return;   
            }
        }
        memcpy(p, ptmp, sizeof(p));
        memcpy(caught, cbefore, sizeof(caught));
        if (cur < curMin) {
            curMin = cur;
        }
    }
}

int main() {
    cin >> t;
    for (long long test = 1; test <= t; test++) {
        curMin = DBL_MAX;;
        cin >> y >> n;
        memset(caught, 0, sizeof(caught));
        for (int i = 0; i < n; i++) {
            cin >> p[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> s[i];
        }

        getMin(1, 0.0, 0, 0.0);
        // cout << endl;
        getMin(-1, 0.0, 0, 0.0);
        cout << "Case #" << test << ": " << setprecision(15) << curMin << endl;
    }
}