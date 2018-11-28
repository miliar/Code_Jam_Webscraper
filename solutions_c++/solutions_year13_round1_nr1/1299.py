#include <iostream>
#include <cmath>

using namespace std;

unsigned long long t;
unsigned long long r;
long double root1, root2;
bool overflowed;

void work() {
    long double tmp1 = r;
    tmp1 /= 2;
    tmp1 = 0.25 - tmp1;
    long double tmp2 = r;
    tmp2 /= 4;
    tmp2 *= r;
    if (tmp2 > 100000000000000LL) overflowed = true;
    tmp2 += 1 / 16.0;
    long double tmp3 = r;
    tmp3 /= 4.0;
    tmp2 -= tmp3;
    long double tmp4 = t;
    tmp4 /= 2.0;
    tmp2 += tmp4;
    root1 = tmp1 - sqrt(tmp2);
    root2 = tmp1 + sqrt(tmp2);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int TT;
    cin >> TT;
    for (int tc = 1; tc <= TT; tc++) {
        cin >> r;
        cin >> t;
        overflowed = false;
        work();
        if (overflowed) root2 -= 0.00000000000001;
        long long ir1 = floor(root1);
        long long ir2 = floor(root2);
        cout << "Case #" << tc << ": ";
        cout << ir2 << endl;
    }
    return 0;
}
