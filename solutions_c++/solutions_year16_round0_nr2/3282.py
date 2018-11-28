/*
* @Author: Yinlong Su
* @Date:   2016-04-08 18:46:52
* @Last Modified by:   Yinlong Su
* @Last Modified time: 2016-04-09 10:04:38
*/

#include <iostream>
#include <stdio.h>
#include <string.h>

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

int main(){
    FILE *fin = freopen("B-large.in", "r", stdin);
    FILE *fout = freopen("B-large.out", "w", stdout);

    ULL T;
    int len;
    int ss[200];

    cin >> T;
    for (int i = 0; i < T; i++) {
        string s;
        cin >> s;
        len = s.length();
        memset(ss, 0, 200 * sizeof(int));
        for (int j = 0; j < len; j++)
            ss[j] = (s[j] == '-' ? 0 : ~0);
        int t = len - 1, f = 0;
        while (t >= 0) {
            if (ss[t] != 0) {
                t--;
                continue;
            }
            for (int j = 0; j <= t; j++)
                ss[j] = ~ss[j];
            f++;
        }
        cout << "Case #" << (i + 1) << ": "<< f << endl;

    }
    return 0;
}