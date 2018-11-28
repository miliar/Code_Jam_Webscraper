#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <functional>
using namespace std;

#define lli long long int

const int N = (int)(3e5 + 20);

int testsCount;
int n;
lli a[N];
lli bestAns, eat;

lli calculate(lli rate) {
    eat = 0;
    lli current = a[0];
    for (int i = 1; i < n; ++i) {
        eat += min(rate, current);
        current = a[i];
    }
    return eat;
}

bool check(lli rate) {
    bool possible = true;
    eat = 0;
    lli current = a[0];
    for (int i = 1; i < n; ++i) {
        current -= rate;
        current = max(current, 0ll);
        if (current > a[i]) return false;
        current = a[i];
    }
    if (possible) {
        bestAns = min(bestAns, rate);
        return true;
    }
    return false;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &testsCount);
    for (int testNumber = 1; testNumber <= testsCount; testNumber++) {
                
        cin >> n;
        lli firstAns = 0;
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
            if (i) firstAns += max(0ll, a[i - 1] - a[i]);
        }
        
        lli l = 0, r = (1 << 30);
        bestAns = r;
        while (r - l > 1) {
            int m = (l + r) / 2;
            if (check(m)) r = m;
            else l = m;
        }
        check(l);
        check(r);

        printf("Case #%d: ", testNumber);
        cout << firstAns << ' ' << calculate(bestAns);
        cout << endl;
    }
}