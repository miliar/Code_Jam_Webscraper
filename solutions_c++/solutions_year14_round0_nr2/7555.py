#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include <utility>

using namespace std;

double plusOneStep(double f, double x, double c, double prodPerS, double totalSec) {
    totalSec += c / prodPerS;
    prodPerS += f;
    totalSec += x / prodPerS;
    return totalSec;
}

double noBuyFirm(double f, double x, double prodPerS, double totalSec) {
    return totalSec + (x / prodPerS);
}

int main() {
//	freopen("date.in", "r", stdin);
//	freopen("date.out","w", stdout);

    int t;
    double c, f, x;

    cin >> t;
    for(int ti = 1; ti <= t; ti++) {
        cin >> c >> f >> x;
        double prodPerS = 2;
        double totalSec = 0;
        while(true) {
            double plus = plusOneStep(f, x, c, prodPerS, totalSec);
            double noBuy = noBuyFirm(f, x, prodPerS, totalSec);
            if(plus > noBuy) {
                printf("Case #%d: %.7f\n", ti, noBuy);
                break;
            } else {
                totalSec += c / prodPerS;
                prodPerS += f;
            }
        }
    }
	return 0;
}
