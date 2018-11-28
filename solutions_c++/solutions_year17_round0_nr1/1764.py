#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <cstring>
#include <stdlib.h>
#include <cmath>
#include <map>
using namespace std;

int n,K;
int a[1010];
int main() {
    int C = 1;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> n;
    for (int i = 0;i < n;i ++) {
        string str;
        cin >> str >> K;
        int len = str.size();
        for (int j = 0;j < len;j ++) {
            if (str[j] == '+') {
                a[j] = 1;
            }
            else {
                a[j] = 0;
            }
        }
        int cnt = 0;
        for (int j = 0;j + K - 1 < len;j ++) {
            if (a[j] == 0) {
                cnt ++;
                for (int k = 0;k < K;k ++) {
                    a[j + k] ^= 1;
                }
            }
        }
        bool ok = true;
        for (int j = 0;j < len;j ++) {
            if (a[j] == 0) {
                ok = false;
                break;
            }
        }
        if (!ok) {
            printf("Case #%d: IMPOSSIBLE\n",C ++);
        }
        else {
            printf("Case #%d: %d\n",C ++, cnt);
        }
    }
 }















