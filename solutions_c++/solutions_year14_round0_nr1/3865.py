#include <vector>
#include<cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <deque>
#include <set>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <cassert>
#endif
#include <ctime>
#include <queue>
#include <stack>
#include<iomanip>
#include <sstream>
#include <cmath>
using namespace std;
typedef pair<int, int> PII;
typedef long long ll;

void solve(int ncase) {
    int row1, row2;
    int mark[16] = {0};
    int cnt = 0;
    cin >> row1;
    for(int i = 1; i <= 4; i ++) {
        for(int j = 1; j <= 4; j ++) {
            int x;
            cin >> x;
            if (i == row1) {
                mark[x - 1] = 1;
            }
        }
    }
    cin >> row2;
    int num = 0;
    for(int i = 1; i <= 4; i ++) {
        for(int j = 1; j <= 4; j ++) {
            int x;
            cin >> x;
            if (i == row2) {
                if (mark[x - 1]) {
                    cnt ++;
                    num = x;
                }
            }
        }
    }
    cout << "Case #" << ncase << ": ";
    if (cnt == 1) {
        cout << num << endl;
        return;
    }
    if (cnt == 0) {
        cout << "Volunteer cheated!" << endl;
        return;
    }
    cout << "Bad magician!" << endl;
}
int main() {
    ios::sync_with_stdio(false);
    //cout << setprecision(16) << endl;
#ifdef _zzz_
    freopen("A--small-attempt0.in", "r", stdin);
    freopen("A-out.txt", "w", stdout);
#endif
    int T = 1;
    cin >> T;
    int ncase = 0;
    while(T --) {
        solve(++ ncase);
    }
}
