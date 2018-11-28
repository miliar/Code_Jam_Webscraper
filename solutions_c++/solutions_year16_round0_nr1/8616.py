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
#include <numeric>
#include <stack>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N;
        cin >> N;
        cout << "Case #" << t << ": ";
        if (N == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        int d[10] = {};
        int res = 0;
        for (int k = 1; k < 1000; ++k) {
            int cur = N * k;
            ostringstream s;
            s << cur;
            for (int i = 0; i < s.str().size(); ++i) {
                res += 1 - d[s.str()[i]-'0'];
                d[s.str()[i]-'0'] = 1;
            }
            if (res == 10) {
                cout << cur << endl;
                break;
            }
        }
        if (res == 10)
            continue;
        throw std::runtime_error("Incorrect answer");
        cout << endl;
    }
}
