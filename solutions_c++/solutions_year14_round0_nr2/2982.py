#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    Solution(string problemName) {
        freopen((problemName + ".in").c_str(), "r", stdin);
        freopen((problemName + ".out").c_str(), "w", stdout);
    }

    void solveAllTestCases() {
        cin >> testNumber;
        for (int test = 1; test <= testNumber; ++test) {
            cout << "Case #" << test << ": ";
            solveOneTestCase();
        }
    }

private:
    int testNumber;
    void solveOneTestCase();
};

void Solution::solveOneTestCase() {
    long double c, f, x;
    cin >> c >> f >> x;

    long double prev_time = 0;

    long double ans = 1e20;

    for (int i = 0; prev_time < ans; ++i) {
        ans = min(ans, prev_time + x / (f * i + 2));
        prev_time += c / (f * i + 2);
    }
    cout << setprecision(15) << fixed;
    cout << ans << endl;
}

int main()
{
    Solution solution("B-large");
    solution.solveAllTestCases();
    return 0;
}

