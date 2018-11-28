#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <complex>
#include <limits>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <algorithm>
#include <functional>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <map>
#include <list>
#include <math.h>
#include <set>
#include <stdio.h>
#include <ctype.h>
#include <vector>
#include <sstream>
#include <iomanip>

using namespace std;

int main() {
    cout.precision(7);
    std::cout.setf(std::ios::fixed, std:: ios::floatfield);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        double c, f, x;
        cin >> c >> f >> x;
        double rate = 2.0;
        double timetofarm = 0;
        double res = x / 2;
        for (int farms = 1; farms <= x; ++farms) {
            timetofarm += c / rate;
            res = min(res, timetofarm + x / (rate + f));
            rate += f;
        }
        cout << "Case #" << t << ": " << res << endl;
    }

    return 0;
}