 
#include <iostream>
using namespace std;

int solve(int x) {
    int y = 0, m = 0, t;
    while (m != 0x3ff) {
        y += x;
        for (t = y; t; t /= 10)
            m |= 1 << (t % 10);
    }
    return y;
}

int main() {
    int N, i;
    cin >> N;
    for (i = 0; i < N; i++) {
        int x;
        cin >> x;
        cout << "Case #" << (i + 1) << ": ";
        if (x) cout << solve(x) << endl;
            else cout << "INSOMNIA" << endl;
    }
    return 0;
}
