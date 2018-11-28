#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int main() {
    ifstream ifs("in.in");
    ofstream ofs("out.out");

    int T;
    ifs >> T;
    for (int t = 1; t <= T; ++t) {
        unsigned long long P, Q;
        char temp;
        ifs >> P >> temp >> Q;

        ofs << "Case #" << t << ": ";

        while (P % 2 == 0) {
            P /= 2;
            Q /= 2;
        }

        if (Q % P == 0) {
            Q /= P;
            P = 1;
        }

        int times = 0;
        unsigned long long Q2 = Q;
        while (Q2 > 1) {
            if (Q2 % 2 != 0) {
                times = -1;
                break;
            }

            Q2 /= 2;
            ++times;
        }

        if (times == -1) {
            ofs << "impossible" << endl;
            continue;
        }

        bool output = false;
        for (int i = 1; i <= 40; ++i) {
            if (P < Q / 2) {
                P *= 2;
            } else {
                output = true;
                ofs << i << endl;
                break;
            }
        }

        if (!output) {
            ofs << "impossible" << endl;
        }
    }

    return 0;
}
