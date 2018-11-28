/*******************************************************************************
	> File Name: a.cpp
	> Author: sillyplus 
	> Mail: oi_boy@sina.cn 
	> Created Time: Sat Apr 11 07:16:28 2015
*******************************************************************************/

#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>

using namespace std;

const int MAXN = 1010;

int sum[MAXN];

int main() {
    int t;
    cin >> t;
    for (int k = 1; k <= t; k++) {
        memset(sum, 0, sizeof(sum));
        int l;
        cin >> l;
        string s;
        cin >> s;
        int ans = 0;
        sum[0] = s[0] - '0';
        for (int i = 1; i <= l; i++) {
            if (s[i] != '0') {
                ans = max(ans, (i - sum[i-1]));
            }
            sum[i] = s[i] - '0';
            sum[i] += sum[i-1];
        }
        printf("Case #%d: %d\n", k, ans);
        
    }
    return 0;
}
