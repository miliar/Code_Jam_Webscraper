#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <cmath>

using namespace std;

using i64 = long long;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    scanf("%d\n", &tests);

    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";

        i64 k, c, s;
        cin >> k >> c >> s;

        i64 shift = 1;
        for (int i = 0; i < c - 1; i++) {
            shift *= k;
        }

        i64 pos = 1;
        for (int i = 0; i < k; i++) {
            cout << pos << " ";
            pos += shift;
        }
        cout << endl;
    }
}