//
//  main.cpp
//  CoinJamGCJ
//
//  Created by 莫润昌 on 16/4/9.
//  Copyright © 2016年 莫润昌. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int num[40];
long long ans[11];
int main(int argc, const char * argv[]) {
    int n, m, i, j, t;
    ios::sync_with_stdio(false);
    freopen("C-small-attempt0.in","r",stdin);
    freopen("a.txt","w",stdout);
    cin >> t;
    cin >> n >> m;
    cout << "Case #" << t << ":"<< endl;
    memset(num, 0, sizeof num);
    num[n - 1] = 1;
    num[n] = 1;
    num[1] = 1;
    while (num[0] == 0 && m) {
        if (num[n] == 1) {
            memset(ans, 0, sizeof ans);
            bool flag = true;
            long long x;
            for (int base = 2; base <= 10; base++) {
                long long temp = 1;
                x = 0;
                for (i = n; i > 0; i --) {
                    x = x + num[i] * temp;
                    temp = temp * base;
                }
                flag = false;
                for (long long index = 2; index * index <= x; index++) {
                    if (x % index == 0) {
                        ans[base] = index;
                        flag =true;
                        break;
                    }
                }
                if (flag == false) {
                    break;
                }
            }
            if (flag) {
                for (i = 1; i <= n; i++)
                    cout << num[i];
                for (i = 2; i <= 10; i++)
                    cout << " " << ans[i];
                cout << endl;
                m--;
            }

        }
        i = n;
        while (num[i] == 1)
            i--;
        num[i] = 1;
        for (j = i + 1; j <= n; j++) {
            num[j] = 0;
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
