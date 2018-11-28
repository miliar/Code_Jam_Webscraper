#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <set>
#include <map>

using namespace std;

typedef unsigned int ui32;

const int INF = (int)1e+9;
const double EPS = (double)1e-9;

void Solve(int testId) {
    double C, F, X;
    cin >> C >> F >> X;

    double spent = 0.0;
    double income = 2.0;

    double best = X / income + spent;
    for (int steps = int(X/C) + 10; steps > 0; --steps) {
        spent += C / income;
        income += F;
        if (best > X / income + spent + EPS)
            best = X / income + spent;
        else
            break;
    }

    printf("Case #%d: %0.7lf\n", testId, best);
}

int main() {
    int testCount;
    cin >> testCount;
    for (int testId = 1; testId <= testCount; ++testId) {
        Solve(testId);
    }

    return 0;
}

