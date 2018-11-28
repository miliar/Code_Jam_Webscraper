/**
 * jerrym
 * B.cpp
 */

#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <bitset>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pii;

int gInt () {
    int i;
    scanf("%d", &i);
    return i;
}

lli gLong () {
    lli i;
    scanf("%lld", &i);
    return i;
}

double gDouble () {
    double i;
    scanf("%lf", &i);
    return i;
}

void quit () {
    fflush(stdout);
    exit(0);
}

double farmCost;
double farmIncome;

double timeToGet (double goal, double rate) {
    if (goal < farmCost || rate > 1E5) {
        return goal / rate;
    }
    return min(farmCost / rate + timeToGet(goal, rate + farmIncome), goal / rate);
}

void solve (int nC) {
    farmCost = gDouble();
    farmIncome = gDouble();
    double totalGoal = gDouble();
    printf("Case #%d: %.8lf\n", nC + 1, timeToGet(totalGoal, 2));
}

int main (int argc, char ** argv) {
    int nC = gInt();
    for (int i = 0; i < nC; ++i) solve(i);
    quit();
}
