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
    int n;
    cin >> n;
    vector <double> a(n), b(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int secondScore = 0;

    set <double> q(b.begin(), b.end());

    for (int i = 0; i < n; ++i) {
        auto it = q.upper_bound(a[i]);
        if (it == q.end()) {
            ++secondScore;
            q.erase(q.begin());
        } else {
            q.erase(it);
        }
    }

    int lo = 0, hi = n;

    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        char ok = true;
        for (int i = n - mid, j = 0; i < n; ++i, ++j) {
            if (a[i] < b[j]) {
                ok = false;
                break;
            }
        }
        if (ok) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    cout << lo << " " << secondScore << endl;
}

int main()
{
    Solution solution("D-large");
    solution.solveAllTestCases();
    return 0;
}

