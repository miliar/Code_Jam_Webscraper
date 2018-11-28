/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

char kbd[8], target[8];
int word[8];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    cout.precision(10);
    cout << scientific;
    int TN;
    cin >> TN;
    int gags = 0;
    for (int T = 1; T <= TN; T++) {
        cerr << T << '/' << TN << endl;
        int k, l, s;
        cin >> k >> l >> s;
        if (k > 7 || s > 7) {
            scanf("%*s%*s");
            cout << "Case #" << T << ": GAG!!! " << k << ' ' << l << ' ' << s << endl;
            cerr << "GAG" << endl;
            gags++;
            continue;
        }
        cin >> kbd >> target;
        int maxpay = 0, total = 0, sumpay = 0;
        for (int i = 0; i < s; ++i) {
            word[i] = 0;
        }
        for (;;) {
//            for (int i = 0; i < s; ++i) {
//                cerr << kbd[word[i]];
//            }
//            cerr << endl;

            int pay = 0;
            for (int i = 0; i + l <= s; ++i) {
                bool f = true;
                for (int j = 0; f && j < l; ++j) {
                    if (kbd[word[i + j]] != target[j]) {
                        f = false;
                    }
                }
                if (f) {
                    pay++;
                }
            }
            if (pay > maxpay) {
                maxpay = pay;
            }
            sumpay += pay;
            total++;

            int i = 0;
            while (i < s && word[i] + 1 == k) {
                word[i++] = 0;
            }
            if (i == s) {
                break;
            }
            word[i]++;
        }
        double ans = maxpay - (double(sumpay) / total);
        cout << "Case #" << T << ": " << ans << endl;
    }
    cerr << "GAGS: " << gags << endl;
    return 0;
}
