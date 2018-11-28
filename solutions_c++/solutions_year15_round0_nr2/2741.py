#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

void solveB() {
    int n, maxp = 1000, result;
    cin >> n;
    vector<int> pancake(n);
    for (int i = 0; i < n; ++i) {
        cin >> pancake[i];
        maxp = max(maxp, pancake[i]);
    }
    result = maxp;
    for (int p = 1; p <= maxp; ++p) {
        int special = 0;
        for (int i = 0; i < n; ++i) {
            special += (pancake[i] - 1) / p;
        }
        result = min(result, special + p);
    }
    cout << result << endl;
}

void solveC() {
    int n, x;
    string str;
    cin >> n >> x >> str;
}

int main() {
    int testcase;
    freopen("/Volumes/Data/download/B-large.in", "r", stdin);
    freopen("/Volumes/Data/download/out.txt", "w", stdout);

    cin >> testcase;
    for (int i = 1; i <= testcase; ++i) {
        cout << "Case #" << i << ": ";
        solveB();
    }
    return 0;
}
