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
    vector <vector <int> > a(4, vector <int>(4));
    vector <vector <int> > b(4, vector <int>(4));

    int first;
    cin >> first;
    --first;

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> a[i][j];
        }
    }

    int second;
    cin >> second;
    --second;

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> b[i][j];
        }
    }

    vector <int> answer;
    sort(a[first].begin(), a[first].end());
    sort(b[second].begin(), b[second].end());
    set_intersection(a[first].begin(), a[first].end(), b[second].begin(), b[second].end(), back_inserter(answer));

    if (answer.empty()) {
        cout << "Volunteer cheated!" << endl;
    } else if (answer.size() == 1) {
        cout << answer[0] << endl;
    } else {
        cout << "Bad magician!" << endl;
    }

}

int main()
{
    Solution solution("A-small");
    solution.solveAllTestCases();
    return 0;
}

