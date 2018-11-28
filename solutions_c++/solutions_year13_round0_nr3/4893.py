/*
 * =====================================================================================
 *
 *       Filename:  gcj.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/13/2013 09:18:14 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  ranaflx
 *        Company:  hit-ACM-Group
 *
 * =====================================================================================
 */

#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;
typedef long long LL;
bool isPalindrome(LL x) {
    LL div = 1;
    while(x / div >= 10) {
        div *= 10;
    }
    while(x) {
        int l = x / div;
        int r = x % 10;
        if(l != r) return false;
        x = (x % div) / 10;
        div /= 100;
    }
    return true;
}

int main() {
    vector<int> pdrm;
    for(LL i = 1;i <= 10000000;i++) {
        if(isPalindrome(i) && isPalindrome(i * i)) {
            pdrm.push_back(i * i);
        }
    }
    int t, A, B;
    scanf("%d", &t);
    for(int cas = 1;cas <= t;cas++) {
        scanf("%d %d", &A, &B);
        int lower = lower_bound(pdrm.begin(), pdrm.end(), A) - pdrm.begin();
        int upper = upper_bound(pdrm.begin(), pdrm.end(), B) - pdrm.begin();
        printf("Case #%d: %d\n", cas, upper - lower);
    }
    return 0;
}
