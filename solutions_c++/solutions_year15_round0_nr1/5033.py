#include <iostream>
#include <stdio.h>
#include<vector>

using namespace std;

int solve(int n, string s) {
    vector<int> vec;
    for (auto &a:s)
        vec.push_back(a - '0');
    int clap = vec[0];
    int ans = 0;
    for (int i = 1; i < n + 1; ++i) {
        if (clap < i) {
            for (int j = 0; j < i; ++j) {
                if (vec[j] < 9) {
                    int added = min(9 - vec[j], i - clap);
                    clap += added;
                    vec[j] += added;
                    ans += added;
                    if (clap == i)
                        break;
                }
            }
        }
        clap += vec[i];
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cerr<<i<<'\n';
        int n;
        string s;
        cin >> n >> s;
        cout << "Case #" << i + 1 << ": " << solve(n, s) << endl;
    }
}