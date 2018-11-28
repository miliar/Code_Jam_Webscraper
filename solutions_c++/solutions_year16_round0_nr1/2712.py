#include <iostream>
#include <algorithm>
using namespace std;

bool tested[10];

bool test(long long x) {
    while (x > 0) {
        tested[x % 10] = true;
        x /= 10;
    }
    for (int i = 0; i < 10; i++) {
        if (!tested[i]) return false;
    }
    return true;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        fill(tested, tested + 10, false);
        int n;
        cin >> n;
        cout << "Case #" << i << ": ";
        if (n == 0) {
            cout << "INSOMNIA";
        } else {
            long long ii = 1;
            while (!test(ii * n)) ii++;
            cout << ii * n;
        }
        cout << endl;
    }
    return 0;
}

