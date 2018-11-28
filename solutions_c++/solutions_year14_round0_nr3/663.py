#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
//#define NDEBUG
#include <cassert>
using namespace std;
#define memsetz(NAME) memset(NAME, 0, sizeof(NAME))
typedef long long i64;

char mx[50][50];
void main2(){
    int r, c, m;
    bool pos = false;
    cin >> r >> c >> m;
    int digcount = r * c - m;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            mx[i][j] = '*';
        }
    }
    if (digcount == 1) {
        pos = true;
    } else if (r == 1 || c == 1) {
        pos = true;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c && digcount != 0; j++) {
                mx[i][j] = '.';
                digcount -= 1;
            }
        }
    } else {
        for (int rr = 2; rr <= r && !pos; rr++) {
            for (int cc = 2; cc <= c && !pos; cc++) {
                if (rr * cc < digcount) {
                    continue;
                }
                int subnum = rr * cc - digcount;
                if ( ((rr == 2 || cc == 2) && subnum == 0) 
                    || subnum <= (rr - 2) * (cc - 2) ){
                    pos = true;
                    for (int i = 0; i < rr; i++) {
                        for (int j = 0; j < cc; j++) {
                            mx[i][j] = '.';
                        }
                    }
                    for (int i = rr - 1; i >= 2; i--) {
                        for (int j = cc - 1; j >= 2 && subnum != 0; j--) {
                            mx[i][j] = '*';
                            subnum--;
                        }
                    }
                }
            }
        }
    }

    if (pos) {
        mx[0][0] = 'c';
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cout << mx[i][j];
            }
            cout << endl;
        }
    } else {
        cout << "Impossible" << endl;
    }
}
int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ":" << endl;
        main2();
    }
    return 0;
}
