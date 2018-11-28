/*************************************************************************
	> File Name: Qualification_A.cpp
	> Author: BMan
	> Mail: luo-kai-jia@163.com
	> Created Time: 2016年04月09日 星期六 19时25分04秒
 ************************************************************************/

#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int _T;
    scanf("%d", &_T);
    for (int _t = 1; _t <= _T; _t++) {
        int n;
        scanf("%d", &n);
        int digit[10] = {0};
        int cnt = 0;
        for (int i = 1; i <= 100; i++) {
            long long x = 1LL * i * n;
            while(x != 0) {
                int j = x % 10;
                x = x / 10;
                if(digit[j] == 0) {
                    digit[j] = 1;
                    cnt++;
                }
            }
            if (cnt == 10) {
                printf("Case #%d: %lld\n", _t, 1LL * i * n);
                break;
            }
        }
        if (cnt != 10) {
            printf("Case #%d: INSOMNIA\n", _t);
        }
    }
    return 0;
}
