/*
 g++ --std=c++11 -Wl,--stack=0x1000000 C.cc
*/

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <bitset>
#include <gmpxx.h>

using namespace std;

int T, N;

int main()
{
    ios::sync_with_stdio(false);
    cout.precision(8);

    cin >> T;
    for (int t = 1; t <= T; t++) {
        bitset<10> f;
        f.set();
        cin >> N;

        if (N) {
            int s = N;
            for (;;s += N) {
                for (int d = s; d > 0; d /= 10) f.reset(d % 10);

                if (f.any()) continue;
                break;
            }
            cout << "Case #" << t << ": " << s << endl;
        } else {
            cout << "Case #" << t << ": INSOMNIA" << endl;
        }
    }
}
