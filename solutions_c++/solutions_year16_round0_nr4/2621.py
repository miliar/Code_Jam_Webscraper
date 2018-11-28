/*
* @Author: Yinlong Su
* @Date:   2016-04-08 18:46:52
* @Last Modified by:   Yinlong Su
* @Last Modified time: 2016-04-09 12:45:13
*/

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

int main(){
    FILE *fin = freopen("D-small-attempt0.in", "r", stdin);
    FILE *fout = freopen("D-small-attempt0.out", "w", stdout);

    ULL T, K, C, S;
    cin >> T;

    for (ULL i = 0; i < T; i++) {
        cin >> K >> C >> S;

        cout << "Case #" << (i + 1) << ":";
        if (C == 1 && S < K) {
            cout << " IMPOSSIBLE" << endl;
            continue;
        }
        else if (C == 1) {
            for (ULL a = 1; a <= K; a++)
                cout << " " << a;
            cout << endl;
            continue;
        }
        if (S < ((K - 1) / 2) + 1) {
            cout << " IMPOSSIBLE" << endl;
            continue;
        }

        ULL j = 1;
        while (j <= K) {
            if (j == K) {
                cout << " " << j;
                j++;
            }
            else {
                cout << " " << ((j - 1) * K + (j + 1));
                j += 2;
            }
        }
        cout << endl;

    }
    return 0;
}