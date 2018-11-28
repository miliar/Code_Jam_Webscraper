#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <utility>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>
#include <functional>
#include <cmath>

using namespace std;
unsigned long long int t, c, i, j, k, l, m = 0, s = 0, p1;
unsigned long long int d, e;

int main() {
    string s3, s4;
    scanf("%llu", &t);
    int cases = 1;
    while (cases <= t) {
        scanf("%llu", &l);
        string s1[l], s2[l];
        for (i = 0; i < l; i++) {
            cin >> s1[i];
            s2[i] += s1[i] + '=';
        }
        p1 = 0;
        s3.clear();
        for (j = 0; j < s2[0].size(); j++) {
            if (s2[0][j] != s2[0][j + 1]) {
                s3 += s2[0][j];
            }
        }
        for (i = 1; i < l; i++) {
            s4.clear();
            for (j = 0; j < s2[i].size(); j++) {
                if (s2[i][j] != s2[i][j + 1]) {
                    s4 += s2[i][j];
                }
            }
            if (s4.size() != s3.size()) {
                p1 = 1;
                break;
            } else {
                for (j = 0; j < s3.size(); j++) {
                    if (s3[j] != s4[j]) {
                        p1 = 1;
                        break;
                    }
                }
                if (p1 == 1) {
                    break;
                }
            }
        }
        if (p1 == 1) {
            printf("Case #%d: Fegla Won\n", cases);
            cases++;
            continue;
        } else {
            d = 0, e = 100000000;
            long int a[l][100];
            for (i = 0; i < l; i++) {
                for (j = 0; j < 100; j++) {
                    a[i][j] = 0;
                }
            }
            for (i = 0; i < l; i++) {
                int k = 0;
                string qw = s1[i] + '=';
                for (j = 0; j < qw.size(); j++) {
                    if (s1[i][j] == s1[i][j + 1]) {
                        a[i][k]++;
                    } else {
                        a[i][k]++;
                        k++;
                    }
                }
            }
            for (i = 0; i < l; i++) {
                d = 0;
                for (j = 0; j < l; j++) {
                    for (k = 0; k < s1[i].size(); k++) {
                        d += abs(a[i][k] - a[j][k]);
                    }
                }
                e = min(d, e);
            }
            string x = s1[0] + '=';
            int fin = 0;
            for (i = 0; i < s1[0].size() - 1; i++) {
                if (s1[0][i] != s1[0][i + 1])
                    fin++;
            }
            fin++;
            d = 0;
            for (i = 0; i < l; i++) {
                int o = s1[i].size();
                d += abs(o - fin);
            }
            e = min(d, e);
            printf("Case #%d: %llu\n", cases, e);
        }
        cases++;
    }
    return 0;
}
