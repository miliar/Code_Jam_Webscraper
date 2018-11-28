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
        string s;
        cin >> s;
        int res = 1;
        for (int i = 1; i < s.size(); ++i) {
            if (s[i] != s[i-1]) {
                res++;
            }
        }
        cout << "Case #" << t << ": ";
        if (s.back() == '+')
            cout << res - 1;
        else
            cout << res;
        cout << endl;
    }
}
