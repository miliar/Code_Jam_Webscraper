/*
* @Author: Yinlong Su
* @Date:   2016-04-08 18:46:52
* @Last Modified by:   Yinlong Su
* @Last Modified time: 2016-04-09 10:07:15
*/

#include <iostream>
#include <stdio.h>
#include <string.h>

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

int main(){
    FILE *fin = freopen("A-large.in", "r", stdin);
    FILE *fout = freopen("A-large.out", "w", stdout);

    ULL T, N;
    char h[10];

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        if (!N) {
            cout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
            continue;
        }
        int remain = 10;
        ULL K = 0;
        memset(h, 0, 10 * sizeof(char));
        while (remain != 0) {
            K += N;
            ULL KK = K;
            while (KK != 0) {
                int digit = KK % 10;
                if (h[digit] == 0)
                    remain--;
                h[digit] = 1;
                KK /= 10;
                if (digit == 0 && h[0] == 0) {
                    h[0] = 1;
                    remain--;
                }
            }
        }
        cout << "Case #" << (i + 1) << ": " << K << endl;
    }
    return 0;
}