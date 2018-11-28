//
//  main.cpp
//  151aa
//
//  Created by dawn on 15-4-18.
//  Copyright (c) 2015å¹?dawn. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t,i = 0;
    cin >> t;
    while (i++ < t) {
        cout << "Case #" << i << ": ";
        long long n, j=0, ele;
        cin >> n;
        vector<int> m;
        while (j++<n) {
            cin >> ele;
            m.push_back(ele);
        }
        long long max = 0;
        long long ans1 = 0, ans2 = 0;
        for (j = 0; j < n-1; ++j) {
            int sub = m[j]-m[j+1];
            if (sub>max)
                max = sub;
            if (sub>0) {
                ans1 += sub;
            }
        }
        for (j = 0; j < n-1; ++j) {
            if (m[j]<max) {
                ans2 += m[j];
            }
            else
                ans2 += max;
        }

        cout << ans1 << " " << ans2 << endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
