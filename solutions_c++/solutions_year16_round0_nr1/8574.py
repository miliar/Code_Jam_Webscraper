/*******************************************************************************
	> File Name: a.cpp
	> Author: sillyplus 
	> Mail: oi_boy@sina.cn 
	> Created Time: Sun Apr 10 01:27:16 2016
*******************************************************************************/

#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[]) {
    int t, tt = 0;
    cin >> t;
    while (t--) {
        tt++;
        long long n;
        long long cnt[10] = {0};
        cin >> n;
        long long kn = n;
        if (n) {
            while (1) {
                long long tmp = kn;
                while (tmp) {
                    cnt[tmp % 10]++;
                    tmp /= 10;
                }
                bool flag = true;
                for (int i = 0; i < 10; ++i) {
                    if (cnt[i] == 0) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    break;
                } else {
                    kn += n;
                }
            }
            printf("Case #%d: %lld\n", tt, kn);
        } else {
            printf("Case #%d: INSOMNIA\n", tt);
        }
        
    }
    return 0;
}
