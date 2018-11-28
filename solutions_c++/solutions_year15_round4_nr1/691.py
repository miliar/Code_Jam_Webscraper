#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

int R, C;
string vs[110];

pair<int, int> get_dir(char ch) {
    if (ch == '>') {
        return make_pair(0, 1);
    } else if (ch == 'v') {
        return make_pair(1, 0);
    } else if (ch == '^') {
        return make_pair(-1, 0);
    } else if (ch == '<') {
        return make_pair(0, -1);
    }
}

int ddd[4][2] = {0,1, 1,0, 0,-1, -1,0};

int main() {
    freopen("C:\\Users\\dd\\Downloads\\A-large.in", "r", stdin);
    freopen("C:\\Users\\dd\\Downloads\\A-large.out", "w", stdout);

    int Te; cin >> Te;
    for (int te = 1; te <= Te; te ++) {


        cin >> R >> C;
        for (int i = 0; i < R; i ++) {
            cin >> vs[i];
        }
        //memset(vst, false, sizeof(vst));
        int ans = 0;
        for (int i = 0; i < R; i ++) {
            for (int j = 0; j < C; j ++) {
                if (vs[i][j] == '.') {
                    continue;
                }
                PII dir = get_dir(vs[i][j]);
                bool need_change = false;
                for (int len = 1; len < 110; len ++) {
                    int ti = i + len * dir.first;
                    int tj = j + len * dir.second;
                    if (ti < 0 || ti >= R || tj < 0 || tj >= C) {
                        need_change = true;
                        break;
                    }
                    if (vs[ti][tj] != '.') {
                        break;
                    }
                }
                //cout << i << ' ' << j << endl;
                if (need_change) {
                    ans++;
                    bool find = false;
                    for (int d = 0; d < 4; d ++) {
                        for (int len = 1; len < 110; len ++) {
                            int ti = i + ddd[d][0] * len;
                            int tj = j + ddd[d][1] * len;
                            if (ti < 0 || ti >= R || tj < 0 || tj >= C) {
                                break;
                            }
                            if (vs[ti][tj] != '.') {
                                find = true;
                            }
                        }
                    }
                    if (!find) {
                        ans = 1000000;
                    }
                }
            }
        }


        printf("Case #%d: ", te);
        if (ans > 100000) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", ans);
        }
    }
    //system("pause");
}