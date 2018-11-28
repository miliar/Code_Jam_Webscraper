//
//  Deceitful.cpp
//  
//
//  Created by John Nevard on 4/12/14.
//
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<double> VD;

int honest(const VD& na, const VD& ke) {
    int n = na.size();
    VD a(na), e(ke);
    sort(a.begin(), a.end());
    sort(e.begin(), e.end());
    int score = 0;
    int k = 0;
    for (int i = 0; i < n; ++i) {
        double x = a[i];
        while (k < n && e[k] < x) ++k;
        if (k < n)
            ++k;
        else
            ++score;
    }
    return score;
}

int deceitful(const VD& na, const VD& ke) {
    int n = na.size();
    VD a(na), e(ke);
    sort(a.begin(), a.end());
    sort(e.begin(), e.end());
    int score = 0;
    int lo = 0, hi = n - 1;
    for (int i = 0; i < n; ++i) {
        double x = a[i];
        if (x < e[lo])
            --hi;
        else {
            ++lo;
            ++score;
        }
    }
    return score;
}

int main() {
    int nc;
    cin >> nc;
    for (int i = 1; i <= nc; ++i) {
        int n;
        cin >> n;
        VD na(n), ke(n);
        for (int j = 0; j < n; ++j)
            cin >> na[j];
        for (int j = 0; j < n; ++j)
            cin >> ke[j];
        int y = deceitful(na, ke);
        int z = honest(na, ke);
        printf("Case #%d: %d %d\n", i, y, z);
    }
    return 0;
}