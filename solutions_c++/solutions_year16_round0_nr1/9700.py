#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;
    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
        long long n;
        cin >> n;

        if (n == 0) {
            cout << "Case #" << tnum + 1 << ": INSOMNIA" << endl;
        } else {
            set <int> digits;
            long long i;
            for (i = 1; digits.size() < 10u; i++) {
                long long cur = i * n;
                while (cur > 0) {
                    digits.insert(cur % 10);
                    cur /= 10;
                }
            }

            cout << "Case #" << tnum + 1 << ": " << (i - 1) * n << endl;
        }
    }

    return 0;
}