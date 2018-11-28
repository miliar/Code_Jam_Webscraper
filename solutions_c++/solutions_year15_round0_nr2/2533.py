#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <array>
#include <map>

using namespace std;


int solve(int n, vector<int>& v) {
    int ans = v[n - 1];
    for (int s = 1; s < ans; s++) {
        int breaks = 0;
        for (int& x : v) {
            if (x > s) {
                breaks += (x / s) + (x % s >0) - 1;
            }
        }
        ans = min(ans, s + breaks);
    }
    return ans;
}

int main() {
    ifstream cin("test.in");
    ofstream cout("test.out");
    int T;
    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int D;
        cin >> D;
        vector<int> p(D);
        for (int i = 0; i < D; i++) {
            cin >> p[i];
        }
        sort(begin(p), end(p));
        cout << "Case #" << testCase << ": " << solve(D, p) << "\n";
    }
    return 0;
}
