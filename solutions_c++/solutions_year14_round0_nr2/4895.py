#include "stdafx.h"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <chrono>
#include <string>
#include <climits>
#include <cstring>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define MAX 100000

class Solution {
public:
    Solution() {
        input = freopen("data.in", "r", stdin);
        output = freopen("data.out", "w", stdout);
    }

    void solve() {
        int T;
        cin >> T;
        for (int i = 1; i <= T; i++)  {
            cout << "Case #" << i << ": " << fixed << setprecision(7) << solveCase() << endl;
        }
    }

private:
    double solveCase() {
        double C, F, X;
        cin >> C >> F >> X;
        double res = DBL_MAX;
        int N = 0;
        while (N < MAX) {
            double cur = 0.0, f = 2.0;
            int i = 0;
            for (; i < N; i++) {
                cur += C / f, f += F;
                if (cur > res) break;
            }
            if (i == N) {
                cur += X / f;
                if (cur < res) res = cur;
            }

            N++;
        }
        return res;
    }

    FILE * input;
    FILE * output;
};

int main() {
    Solution sol;
    sol.solve();
}
