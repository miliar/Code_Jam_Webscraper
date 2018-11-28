/*******************************************************************************
	> File Name: b.cpp
	> Author: sillyplus 
	> Mail: oi_boy@sina.cn 
	> Created Time: Sun Apr 12 00:41:57 2015
*******************************************************************************/

#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const int MAXN = 1010;

int a[MAXN];

int main() {
    int t;
    cin >> t;
    for (int k = 1; k <= t; k++) {
        int n, mx = 0;
        cin >> n;
        for (int i = 0; i < n; i++) { 
            cin >> a[i];
            mx = max(mx, a[i]);
        }
        int ans = mx;
        for (int i = 1; i <= mx; i++) {
            int tmp1 = 0;
            for (int j = 0; j < n; j++) {
                int tmp2 = 0;
                if (a[j] > i)
                    tmp2 = (a[j] % i == 0) ? (a[j] / i - 1) : (a[j] / i);
                tmp1 += tmp2;
            }
            ans = min(ans, i+tmp1);
        }
        printf("Case #%d: %d\n", k, ans);
    }
    return 0;
}
