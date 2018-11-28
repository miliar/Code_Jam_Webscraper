#include <iostream>
#include <string>
#include <cstring>

using namespace std;

string Solve(int n) {
    if (n == 0) {
        return "INSOMNIA";
    }
    int c[10];
    memset(c, 0, sizeof(c));
    int cnt = 0;
    int m = n;
    while (true) {
        for (int j = m; j > 0; j /= 10) {
            cnt += c[j % 10] == 0;
            c[j % 10]++;
        }
        if (cnt == 10) {
            break;
        }
        m += n;
    }
    return to_string(m);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int n;
        cin >> n;
        cout << "Case #" << i << ": " << Solve(n) << "\n";
    }
}