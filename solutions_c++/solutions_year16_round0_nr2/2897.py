//
//  main.cpp
//  RevengeOfThePancakesGCJ
//
//  Created by 莫润昌 on 16/4/9.
//  Copyright © 2016年 莫润昌. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int main(int argc, const char * argv[]) {
    int ans, t, k;
    freopen("B-large.in","r",stdin);
    freopen("a.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin >> t;
    k = 1;
    getchar();
    while (k <= t) {
        ans = 0;
        char s[105];
        cin >> s;
        int j = 0;
        for (int i = 0; i < strlen(s); i++) {
            if (i == 0 && s[i] == '-')
                ans++;
            if (s[i] == '+') {
                j = 1;
            }
            if (s[i] == '-' && j == 1) {
                ans += 2;
                j = 0;
            }
        }
        cout << "Case #" << k << ": ";
        cout << ans << endl;
        k++;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
