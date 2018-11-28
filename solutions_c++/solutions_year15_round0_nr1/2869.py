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

void solve() {
    int n;
    string s;
    cin >> n >> s;
    int need = 0, person = 0;
    for (int i = 0; i <= n; ++i) {
        if (person < i) {
            ++ person;
            ++ need;
        }
        person += s[i] - '0';
    }
    cout << need << endl;
}

int main() {
    int testcase;
    freopen("/Volumes/Data/download/A-large.in", "r", stdin);
    freopen("/Volumes/Data/download/out.txt", "w", stdout);
    cin >> testcase;
    for (int i = 1; i <= testcase; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
