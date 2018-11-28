#include <bits/stdc++.h>

using namespace std;

const int N = 15;
const int J = 50;

int get_divisor(int base, int num) {
    double tmp = sqrt(num);
    for (int i = 2; i <= tmp; i++) {
        if (num % i == 0) {
            return i;
        }
    }
    return -1;
}

int frame = 1 + (1 << 15);
int divi[11];

int main()
{
    freopen("1.txt", "rt", stdin);
    freopen("2.txt", "wt", stdout);
    int c, s, k, t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> k >> c >> s;
        cout << "Case #" << i << ": ";
        for (int j = 1; j <= k; j++) {
            cout << j << ' ';
        }
        cout << '\n';
    }
    return 0;
}
