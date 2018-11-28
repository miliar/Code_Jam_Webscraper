#include <iostream>
#include <queue>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <climits>
#include <string>
#include <cstring>
#include <vector>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

#define fori(i, a, b) for(int (i) = (a); (i) < (b); (i)++)
#define ford(i, a, b) for(int (i) = (a)-1; (i) >= (b); --(i))
#define test(t) while((t)--)
#define MP make_pair
#define mod 1000000007

map<pair<int, int>, int> dp;
map<char, int> cmap;

int main() {
    dp[MP(1, 2)] = 2;
    dp[MP(1, 3)] = 3;
    dp[MP(1, 4)] = 4;
    dp[MP(1, -2)] = -2;
    dp[MP(1, -3)] = -3;
    dp[MP(1, -4)] = -4;
    dp[MP(-1, -2)] = 2;
    dp[MP(-1, -3)] = 3;
    dp[MP(-1, -4)] = 4;
    dp[MP(-1, 2)] = -2;
    dp[MP(-1, 3)] = -3;
    dp[MP(-1, 4)] = -4;

    dp[MP(2, 2)] = -1;
    dp[MP(3, 3)] = -1;
    dp[MP(4, 4)] = -1;
    dp[MP(2, 3)] = 4;
    dp[MP(2, 4)] = -3;
    dp[MP(3, 4)] = 2;
    dp[MP(3, 2)] = -4;
    dp[MP(4, 2)] = 3;
    dp[MP(4, 3)] = -2;

    dp[MP(-2, 2)] = 1;
    dp[MP(-3, 3)] = 1;
    dp[MP(-4, 4)] = 1;
    dp[MP(-2, 3)] = -4;
    dp[MP(-2, 4)] = 3;
    dp[MP(-3, 4)] = -2;
    dp[MP(-3, 2)] = 4;
    dp[MP(-4, 2)] = -3;
    dp[MP(-4, 3)] = 2;

    dp[MP(2, -2)] = 1;
    dp[MP(3, -3)] = 1;
    dp[MP(4, -4)] = 1;
    dp[MP(2, -3)] = -4;
    dp[MP(2, -4)] = 3;
    dp[MP(3, -4)] = -2;
    dp[MP(3, -2)] = 4;
    dp[MP(4, -2)] = -3;
    dp[MP(4, -3)] = 2;

    dp[MP(-2, -2)] = -1;
    dp[MP(-3, -3)] = -1;
    dp[MP(-4, -4)] = -1;
    dp[MP(-2, -3)] = 4;
    dp[MP(-2, -4)] = -3;
    dp[MP(-3, -4)] = 2;
    dp[MP(-3, -2)] = -4;
    dp[MP(-4, -2)] = 3;
    dp[MP(-4, -3)] = -2;

    cmap['i'] = 2;
    cmap['j'] = 3;
    cmap['k'] = 4;
    ifstream read;
    ofstream write;
    read.open ("C-small-attempt0.in");
    write.open ("a.out");
    int t, ccase = 1;
    read >> t;
    while (ccase <= t) {
        cout << ccase << endl;
        int x, l;
        read >> x >> l;
        string unit, data;
        read >> unit;
        if (x*l < 3) {
            write << "Case #" << ccase << ": " << "NO" << endl;
        } else {
            data = unit;
            fori (i, 0, l-1) {
                data = data + unit;
            }
            int size = data.length();
            //cout << data << endl;
            int ians = 1, jans, kans;
            int i = 0, j, k;
            bool yes = false;
            while (i < size-2) {
                //cout << "here" << endl;
                ians = dp[MP(ians, cmap[data.at(i)])];
                i++;
                while (ians != 2 && i < size-2) {
                    //cout << "here1" << endl;
                    ians = dp[MP(ians, cmap[data.at(i)])];
                    i++;
                }
                if (ians == 2 && i <= size-2) {
                    j = i;
                    jans = dp[MP(1, cmap[data.at(j)])];
                    j++;
                    while (jans != 3 && j < size-1) {
                        //cout << size << " here2 " << j << endl;
                        jans = dp[MP(jans, cmap[data.at(j)])];
                        j++;
                    }
                    if (jans == 3 && j <= size-1) {
                        k = j;
                        //cout << k << " gotta" << endl;
                        kans = dp[MP(1, cmap[data.at(k)])];
                        k++;
                        while (k < size) {
                            //cout << "here3" << endl;
                            kans = dp[MP(kans, cmap[data.at(k)])];
                            k++;
                        }
                        if (kans == 4) {
                            yes = true;
                            break;
                        }
                    }
                } else {
                    break;
                }
            }
            if (yes) {
                write << "Case #" << ccase << ": " << "YES" << endl;
            } else {
                write << "Case #" << ccase << ": " << "NO" << endl;
            }
        }
        ccase++;
    }
    return 0;
}
