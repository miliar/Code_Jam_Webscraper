#include <iostream>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>
#include <queue>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int func(vector<int> P) {
    auto res = max_element(P.begin(), P.end());
    //cout << *res << endl;
    int result = *res;
    int res2 = result;
    if (result > 3) {
        P.push_back(0);
        auto res = max_element(P.begin(), P.end());
        *res = result - result/2;
        P.back() = result/2;
        res2 = min(res2, func(P) + 1);
        if (result > 6) {
        P.back() = result / 3;
        *res = result - result/3;
        res2 = min(res2, func(P) + 1);
        }
    }
    return res2;
}

int main() {
    //ifstream cin("in.txt");
    //ofstream cout("out.txt");
    int T = 0;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        int result = 0;

        int D = 0;
        cin >> D;
        vector<int> P(D);
        for (int& p: P) {
            cin >> p;
        }

        result = func(P);

        cout << result << endl;
    }
}
