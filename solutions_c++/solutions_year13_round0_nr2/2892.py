/* 
 * File:   main.cpp
 * Author: waleed
 *
 * Created on April 13, 2013, 2:01 AM
 */

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <fstream>
#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define pi acos(-1.0)
#define N 1000000
#define LL long long

#define For(i, a, b) for( int i = (a); i < (b); i++ )
#define Fors(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fore(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Set(a, s) memset(a, s, sizeof (a))
#define Read(r) freopen(r, "r", stdin)
#define Write(w) freopen(w, "w", stdout)

#define isOn(S, j) (S & (1 << j))
#define setBit(S, j) (S |= (1 << j))
#define clearBit(S, j) (S &= ~(1 << j))
#define toggleBit(S, j) (S ^= (1 << j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1 << n) - 1)

using namespace std;

int main(int argc, char** argv) {
    fstream cin("in.in", ios::in);
    fstream cout("out.out", ios::out);
    int cas;
    cin >> cas;
    for (int cs = 1; cs <= cas; cs++) {
        int n, m;
        cin >> n >> m;
        int boa[102][102];
        int mini = INF_MAX, maxi = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> boa[i][j];
                if (boa[i][j] < mini) mini = boa[i][j];
                if (boa[i][j] > maxi) maxi = boa[i][j];
            }
        }

        bool pos = true;
        for (int q = mini; q <= maxi && pos; q++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m && pos; j++) {
                    if (boa[i][j] == q) {
                        bool temp = true;
                        for (int k = 0; k < n; k++) {
                            if (boa[k][j] > q) {
                                temp = false;
                            }
                        }
                        if (!temp) {
                            temp = true;
                            for (int k = 0; k < m; k++) {
                                if (boa[i][k] > q) {
                                    temp = false;
                                }
                            }
                            if (!temp) {
                                pos = false;
                            }
                        }
                    }
                }
            }
        }

        if (pos) {
            cout << "Case #" << cs << ": YES" << endl;
        } else {
            cout << "Case #" << cs << ": NO" << endl;
        }
    }

    return 0;
}
