//
//  main.cpp
//  CountingSheepForGCJ
//
//  Created by 莫润昌 on 16/4/9.
//  Copyright © 2016年 莫润昌. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
int f[10];
bool countNumber(int n) {
    while (n != 0) {
        f[n % 10] = 1;
        n = n / 10;
    }
    bool ans = true;
    for (int i = 0; i <= 9; i++) {
        if (f[i] == 0) {
            ans =false;
            break;
        }
    }
    return ans;
}
int main(int argc, const char * argv[]) {
    freopen("A-large.in","r",stdin);
    freopen("a.txt","w",stdout);
    ios::sync_with_stdio(false);
    int flag, t, k, n, temp;
    cin >> t;
    k = 1;
    while (k <= t) {
        cin >> n;
        temp = n;
        if (n == 0) {
            cout << "Case #" << k << ": ";
            cout << "INSOMNIA" << endl;
            k++;
            continue;
        }
        memset(f, 0, sizeof f);
        flag = false;
        flag = countNumber(n);
        while (flag == false) {
            n = n + temp;
            flag = countNumber(n);
        }
        cout << "Case #" << k << ": ";
        cout << n << endl;
        k++;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
