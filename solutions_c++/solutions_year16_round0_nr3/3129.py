#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <float.h>

using namespace std;

#define REP(i, from, to) for (int i = (from); i < (to); ++i)
#define FOR(i, n) REP(i, 0, (n))
#define ALL(x) x.begin(), x.end()
#define SIZE(x) (int)x.size()
#define PB push_back
#define MP make_pair

typedef long long i64;

typedef vector<int>    VI;
typedef vector<VI>     VVI;
typedef vector<string> VS;
typedef vector<VS>     VVS;
typedef pair<int, int> PII;

bool solve(int n, string& binary, vector<i64>& divisors) {
    if (n % 2 == 0) return false;

    divisors.resize(9);
    REP (d, 2, 11) {
        int k = n;
        i64 number = 0;
        i64 p = 1;
        while (k) {
            if (d == 2) {
                binary = char((k & 1) + '0') + binary;
            }
            number += (k & 1) * p;
            p *= d;
            k >>= 1;
        }

        bool ok = false;
        for (i64 m = 2; m * m <= number; ++m) {
            if (number % m == 0) {
                divisors[d - 2] = m;
                //cout << d << " " << number << " " << m << " " << number % m << endl;
                ok = true;
                break;
            }
        }

        if (!ok) return false;
    }

    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);


    int tests;
    cin >> tests;


    int n, k;
    cin >> n >> k;

    cout << "Case #1:\n";
/*
    {
        n = 6; /// 100011
        vector<i64> divisors;
        string binary;
        if (solve((1 << 5) + 3, binary, divisors)) {
            --k;
            cout << binary;
            FOR (j, SIZE(divisors)) cout << " " << divisors[j];
            cout << endl;
        }

        return 0;
    }
*/
     REP (i, 1, 1 << (n - 1)) {
            if (!k) break;
            vector<i64> divisors;
            string binary;
            int number = i + (1 << (n - 1));
            if (solve(number, binary, divisors)) {
                --k;
                cout << binary;
                FOR (j, SIZE(divisors)) cout << " " << divisors[j];
                cout << endl;
            }
     }

    return 0;
}
