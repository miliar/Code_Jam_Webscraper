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
            int N;
            cin >> N;
            vector<double> ns(N, 0.0), ks(N, 0.0);
            for (int j = 0; j < N; j++) cin >> ns[j];
            for (int j = 0; j < N; j++) cin >> ks[j];
            sort(begin(ns), end(ns));
            sort(begin(ks), end(ks));
            cout << "Case #" << i << ": " << solveCase1(N, ns, ks) << " " << solveCase2(N, ns, ks) << endl;
        }
    }

private:
    int solveCase1(int N, vector<double> ns, vector<double> ks) {
        int i = 0;
        for (; i < N; i++) {
            int j = 0;
            for (; i + j < N; j++) {
                if (ns[i + j] < ks[j]) break;
            }
            if (i + j == N) break;
        }

        return N - i;
    }


    int solveCase2(int N, vector<double> ns, vector<double> ks) {
        int i = 0, j = 0;
        while (i < N) {
            while (j < N && ns[i] > ks[j]) j++;
            if (j == N) break;
            i++; j++;
        }
        return N - i;
    }

    FILE * input;
    FILE * output;
};

int main() {
    Solution sol;
    sol.solve();
}
