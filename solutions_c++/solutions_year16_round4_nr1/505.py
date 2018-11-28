#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <tuple>
#include <map>
#include <set>

#include <gmpxx.h>
#include <QtGlobal>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned long ul;

#define MAXINT 0x7FFFFFFF

void disp(int P, int R, int S, int N) {
    if (!N) {
        if (P) cout << "P";
        else if (R) cout << "R";
        else cout << "S";
        return;
    }
    int mN = N - 1;
    int tmp = (1 << mN) / 3;
    int lP = tmp, lR = tmp, lS = tmp, rP = tmp, rR = tmp, rS = tmp;
    tmp <<= 1;
    P -= tmp;
    R -= tmp;
    S -= tmp;
    switch (P + R + S) {
    case 2:
        if (!P) {
            ++lR;
            ++rS;
        } else if (!R) {
            ++lP;
            ++rS;
        } else {
            ++lP;
            ++rR;
        }
        break;
    case 4:
        if (P == 2) {
            ++lP;
            ++lR;
            ++rP;
            ++rS;
        } else if (R == 2) {
            ++lP;
            ++lR;
            ++rR;
            ++rS;
        } else {
            ++lP;
            ++lS;
            ++rR;
            ++rS;
        }
        break;
    default:
        cerr << "Unexpected error!" << endl;
        return;
    }
    disp(lP, lR, lS, mN);
    disp(rP, rR, rS, mN);
}

int main() {
    int T, N, R, P, S, M, Lt, Rt;
    cin >> T;
    for (int i = 0; i < T;) {
        cin >> N >> R >> P >> S;
        cout << "Case #" << (++i) << ": ";
        M = R + P + S;
        Lt = M / 3;
        Rt = (M + 2) / 3;
        if ((M != (1 << N)) || (R < Lt) || (P < Lt) || (S < Lt) || (R > Rt) || (P > Rt) || (S > Rt)) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        disp(P, R, S, N);
        cout << endl;
    }
    return 0;
}
