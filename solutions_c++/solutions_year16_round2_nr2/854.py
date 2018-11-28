#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <bitset>
#include <queue>
#include <map>


using namespace std;


int n;
string a, b;
long long razn = 0;
long long t = 1;
long long t1 = 1;
long long ans = 2000000000000000000LL;
string ansa, ansb;


void get(int i) {
   // cout << t << endl;
   // cout << razn << endl;
    if (i == 2 * n) {
        //cout << a << ' ' << b << ' ' << razn << endl;
        if (ans > abs(razn)) {
            ansa = a;
            ansb = b;
            ans =  abs(razn);
        } else {
            if (ans == abs(razn)) {
                if (ansa > a) {
                    ansa = a;
                    ansb = b;
                } else {
                    if (ansa == a && ansb > b) {
                        ansb = b;
                    }
                }
            }
        }
        return;
    }
    if (i < n) {
        if (a[i] == '?') {
            for (char c = '0'; c <= '9'; c++) {
                a[i] = c;
                razn += t * (a[i] - '0');
                if (i + 1 != n) {
                    t /= 10LL;
                }   
                get(i + 1);
                 if (i + 1 != n) {
                    t *= 10LL;
                }
                razn -= t * (a[i] - '0');
                a[i] = '?';
            }
        } else {
            razn += t * (a[i] - '0');
          //  cout << razn << endl;
            if (i + 1 != n) {
                t /= 10LL;
            }   
            get(i + 1);
            if (i + 1 != n) {
                t *= 10LL;
            }
            razn -= t * (a[i] - '0');
        }
    } else {
        if (b[i - n] == '?') {
            for (char c = '0'; c <= '9'; c++) {
                b[i - n] = c;
                razn -= t1 * (b[i - n] - '0');
                if (i + 1 != 2 * n) {
                    t1 /= 10LL;
                }
                get(i + 1);
                if (i + 1 != 2 * n) {
                    t1 *= 10LL;
                }
                razn += t1 * (b[i - n] - '0');
                b[i - n] = '?';
            }
        } else {
            razn -= t1 * (b[i - n] - '0');
            if (i + 1 != 2 * n) {
                    t1 /= 10LL;
                }
            get(i + 1);
            if (i + 1 != 2 * n) {
                    t1 *= 10LL;
                }
            razn += t1 * (b[i - n] - '0');
        }
    }
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tt;
    cin >> tt;
    for (int ii = 0; ii < tt; ii++) {
        cin >> a >> b;
        n = (int)a.size();
        long long razn = 0;
        t = 1;    
        t1 = 1;
        for (int i = 0; i < n - 1; i++) {
            t *= 10LL;
            t1 *= 10LL;
        }
        //cout << t << endl;
        razn = 0;
        ans = 2000000000000000000LL;
        get(0);
       // cout << ans << endl;
        // for (int i = 0; i < n; i++) {
        //     if (a[i] != '?' && b[i] != '?') {
        //         razn += t * (a[i] - '0') - t * (b[i] - '0');
        //         t /= 10LL;
        //         continue;
        //     }
        //     if (a[i] == '?' && b[i] == '?') {
        //         if (razn < 0LL) {
        //             long long p = min(9LL, (abs(razn) % t <= t - abs(razn) ? abs(razn) / t: abs(razn) / t + 1LL));
        //             a[i] = '0' + p;
        //             b[i] = '0';
        //         } else  {
        //             long long p = min(9LL, (abs(razn) % t <= t - abs(razn) ? abs(razn) / t: abs(razn) / t + 1LL));
        //             b[i] = '0' + p;
        //             a[i] = '0';
        //         }
        //         razn += t * (a[i] - '0') - t * (b[i] - '0');
        //         t /= 10LL;
        //         continue;
        //     }
        //     if (a[i] == '?') {
        //         razn -= t * (b[i] - '0');
        //         if (razn < 0) {
        //             long long p = min(9LL, (abs(razn) % t <= t - abs(razn) ? abs(razn) / t: abs(razn) / t + 1LL));
        //             a[i] = '0' + p;
        //         } else {
        //             a[i] = '0';
        //         }
        //         razn += t * (a[i] - '0');
        //         t /= 10LL;
        //         continue;
        //     }
        //     razn += t * (a[i] - '0');
        //     if (razn > 0) {
        //         long long p = min(9LL, razn / t);
        //         b[i] = '0' + p;
        //     } else {
        //         b[i] = '0';
        //     }
        //     razn -= t * (b[i] - '0');
        //     t /= 10LL;
        // }
         cout << "Case #" << ii + 1 << ": " << ansa << ' ' << ansb << endl;
    }
    return 0;
}
