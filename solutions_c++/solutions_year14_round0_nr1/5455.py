#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <set>
#include <map>

using namespace std;

typedef unsigned int ui32;

const int INF = (int)1e+9;
const double EPS = (double)1e-9;

void ReadPos(set<int>& vals) {
    int ans;
    cin >> ans;
    for (int rowId = 1; rowId <= 4; ++rowId) {
        for (int col = 1; col <= 4; ++col) {
            int num;
            cin >> num;
            if (rowId == ans)
                vals.insert(num);
        }
    }
}

void Solve(int testId) {
    set<int> s1, s2;
    ReadPos(s1);
    ReadPos(s2);
    vector<int> inter(4);
    vector<int>::iterator it = set_intersection(s1.begin(), s1.end(),
            s2.begin(), s2.end(), inter.begin());
    int sz = it - inter.begin();
    cout << "Case #" << testId << ": ";
    if (sz == 1) {
        cout << inter[0];
    } else
    if (sz > 1) {
        cout << "Bad magician!";
    } else {
        cout << "Volunteer cheated!";
    }
    cout << "\n";
}

int main() {
    int testCount;
    cin >> testCount;
    for (int testId = 1; testId <= testCount; ++testId) {
        Solve(testId);
    }

    return 0;
}

