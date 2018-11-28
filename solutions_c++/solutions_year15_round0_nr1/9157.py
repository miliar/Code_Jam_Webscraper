#include <algorithm>
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    //ifstream cin("f.in");
    //ofstream cout("f.out");
    int tests, n, t = 0; string str;
    for (cin >> tests; tests; -- tests) {
        cin >> n >> str;
        int cnt = 0, add = 0;
        for (int i = 0; i <= n; ++ i) {
            for (int j = 0; j < str[i] - '0'; ++ j) {
                if (cnt + add < i) {
                    add = max(add, i - cnt);
                }
                ++ cnt;
            }
        }
        cout << "Case #" << ++ t << ": " << add << "\n";
    }
    return 0;
}
