#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <limits>
#include <numeric>
#include <map>
#include <unordered_set>
#include <string>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
typedef long long int ll;
typedef long double ld;
const ld p_base = 2;

const ld solve (ld c, ld f, ld x) {
    ld t = 0;
    ld p = p_base;
    for (int cc = 0 ;; ++cc) {
        if (x / p <= c / p +  x / (p + f)) {
            return t + x / p;
        }
        t += c / p;
        p += f;
    }
}

int main() {
    int numberOfCases;
	cin >> numberOfCases;
	for (int testCase = 1; testCase <= numberOfCases; ++testCase) {
        ld c, d, x;
        cin >> c >> d >> x;
		cout << "Case #" << testCase << ": " << fixed << setprecision(7)
            << solve(c, d, x) << endl;
	}
}
