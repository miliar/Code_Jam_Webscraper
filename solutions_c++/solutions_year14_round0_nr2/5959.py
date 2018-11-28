#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void run() {
    double C, F, X;
    cin >> C >> F >> X;
    double t = 0;
    double cps = 2.0;
    while (true) {
        double wait = X / cps;
        double buy = C / cps + X / (cps + F);
        if (wait <= buy) {
            t += wait;
            break;
        }
        t += C / cps;
        cps += F;
    }
    printf("%.7f\n", t);
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ": ";
        run();
    }

}
