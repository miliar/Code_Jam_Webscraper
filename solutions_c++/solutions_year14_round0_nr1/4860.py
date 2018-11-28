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
            cout << "Case #" << i << ": " << solveCase() << endl;
        }
    }

private:
    string solveCase() {
        memset(tb, 0, sizeof(tb));
        calc();
        calc();
        int res = -1;
        for (int k = 1; k <= 16; k++) {
            if (tb[k] == 2) {
                if (res != -1) return "Bad magician!";
                res = k;
            }
        }
        if (res == -1) return "Volunteer cheated!";
        return to_string(res);
    }

    void calc() {
        int N;
        cin >> N;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                int val;
                cin >> val;
                if (i == N - 1) tb[val]++;
            }
        }
    }

    int tb[17];

    FILE * input;
    FILE * output;
};

int main() {
    Solution sol;
    sol.solve();
}
