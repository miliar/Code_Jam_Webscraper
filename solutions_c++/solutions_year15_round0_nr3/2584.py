#include <fstream>
#include <queue>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <assert.h>

using namespace std;

const char ONE = 'h';
const char I = 'i';
const char J = 'j';
const char K = 'k';

char QMUL[4][4] = {
    { ONE, I, J, K },
    { I, -ONE, K, -J },
    { J, -K, -ONE, I },
    { K, J, -I, -ONE }
};

inline char qmul(char a, char b) {
    bool negate = false;
    if ((a < 0 && b > 0) || (a > 0 && b < 0))
        negate = true;
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    a -= ONE;
    b -= ONE;
    if (negate)
        return -QMUL[a][b];
    else
        return QMUL[a][b];
}

bool solve(const string& s) {
    const int N = s.length();

    char sv[N];
    sv[N-1] = s[N-1];
    for (int i = N-2; i >= 2; --i) {
        sv[i] = qmul(s[i], sv[i+1]);
    }

    char r1; int s1;
    for (s1=0, r1=ONE; s1 < N-2; ++s1) {
        r1 = qmul(r1, s[s1]);
        if (r1 == I) {
            char r2; int s2;
            for (s2=s1+1, r2=ONE; s2 < N-1; ++s2) {
                r2 = qmul(r2, s[s2]);
                if (r2 == J) {
                    int s3 = s2 + 1;
                    char r3 = sv[s3];
                    if (r3 == K)
                        return true;
                }
            }
        }
    }
    return false;
}

int main() {
    ifstream input("C-small-attempt1.in");
    ofstream output("C-small-attempt1.out");

    int T, tc = 1;
    input >> T;
    while (T--) {
        int L, X;
        input >> L >> X;
        string sl, s;
        input >> sl;
        // Special case: not enough chars
        if (L*X < 3) {
            output << "Case #" << tc++ << ": NO" << endl;
            continue;
        }
        // Build string to be evaluated
        for (int i = 0; i < X; ++i)
            s += sl;
        output << "Case #" << tc++ << ": " << (solve(s) ? "YES" : "NO") << endl;
    }
}
