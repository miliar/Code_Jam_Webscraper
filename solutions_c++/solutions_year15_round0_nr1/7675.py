#include <iostream>
#include <algorithm>
#include <functional>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <tuple>
#include <cstdio>
#include <cstdlib>
#include <cmath>

const int N = 1001;

int shy_levels[N];

using namespace std;

void solve(int tcase, int n) {
    int pre_sum = 0;
    int how_much_to_add = 0;
    for(int i = 0; n > i; i++) {
        if(shy_levels[i] != 0 && i > pre_sum) {
            how_much_to_add += i - pre_sum;
            pre_sum += i - pre_sum;
        }
        pre_sum += shy_levels[i];
    }
    cout << "Case #" << tcase + 1 << ": " << how_much_to_add << endl;
}

int main(int argc, char *argv[]) {
    int t;
    cin >> t;
    int max_s;
    string s;
    for(int i = 0; t > i; i++) {
        cin >> max_s;
        cin >> s;
        max_s += 1;
        for(int j = 0; max_s > j; j++) {
            shy_levels[j] = (int)(s[j] - '0');
        }
        solve(i, max_s);
    }
    return 0;
}