#include <cstdio>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <stack>
#include <map>
#include <queue>
#include <string>
#include <list>
#include <set>
#include <unordered_map>
#include <cstring>
#include <ctime>
#include <bitset>
#include <cassert>
using namespace std;

#include "Infint.h"
//#include "euler.h"

string s[15][3]; // 'R' wins, 'P' wins, 'S' wins
int rc[15][3] = {0};
int pc[15][3] = {0};
int sc[15][3] = {0};

int main() {
    freopen("/Users/tianyi/Desktop/input.txt", "r", stdin);
//    freopen("/Users/tianyi/Desktop/output.txt", "w", stdout);
    s[0][0] = "R";
    s[0][1] = "P";
    s[0][2] = "S";
    rc[0][0] = 1;
    pc[0][1] = 1;
    sc[0][2] = 1;
    for (int i = 1; i <= 12; i++) {
//        printf("n = %d\n", i);
        for (int j = 0; j < 3; j++) {
            s[i][j] = "";
            vector<string> v;
            if (j == 0) {
                v.push_back(s[i-1][0]);
                v.push_back(s[i-1][2]);
                rc[i][j] = rc[i-1][0] + rc[i-1][2];
                pc[i][j] = pc[i-1][0] + pc[i-1][2];
                sc[i][j] = sc[i-1][0] + sc[i-1][2];
            }
            else if (j == 1) {
                v.push_back(s[i-1][0]);
                v.push_back(s[i-1][1]);
                rc[i][j] = rc[i-1][0] + rc[i-1][1];
                pc[i][j] = pc[i-1][0] + pc[i-1][1];
                sc[i][j] = sc[i-1][0] + sc[i-1][1];
            }
            else if (j == 2) {
                v.push_back(s[i-1][1]);
                v.push_back(s[i-1][2]);
                rc[i][j] = rc[i-1][1] + rc[i-1][2];
                pc[i][j] = pc[i-1][1] + pc[i-1][2];
                sc[i][j] = sc[i-1][1] + sc[i-1][2];
            }
            
            sort(v.begin(), v.end());
            s[i][j] = v[0] + v[1];
//            cout << s[i][j] << endl;
//            printf("%d %d %d\n", rc[i][j], pc[i][j], sc[i][j]);
        }
    }
    int tc; scanf("%d", &tc);
    for (int tcn = 1; tcn <= tc; tcn++) {
        printf("Case #%d: ", tcn);
        int n, rr, pp, ss;
        scanf("%d%d%d%d", &n, &rr, &pp, &ss);
        bool possible = false;
        for (int i = 0; i < 3; i++) {
            if (rc[n][i] == rr && pc[n][i] == pp && sc[n][i] == ss) {
                possible = true;
                cout << s[n][i] << endl;
                break;
            }
        }
        if (!possible) cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}