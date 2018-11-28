#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;
typedef long long LL;
const double EPS = 1e-8;
const int INF = 0x3f3f3f3f;

char note[5][5];

bool judge(char ch) {
    vector<pair<int, int> > vex;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (note[i][j] == 'T') {
                note[i][j] = ch;
                vex.push_back(pair<int, int>(i, j));
            }
        }
    }
    for (int i = 0; i < 4; i++) {
        if (note[i][0] == note[i][1] && note[i][1] == note[i][2] && note[i][2] == note[i][3] && note[i][3] == ch) {
            return true;
        }
    }
    for (int i = 0; i < 4; i++) {
        if (note[0][i] == note[1][i] && note[1][i] == note[2][i] && note[2][i] == note[3][i] && note[3][i] == ch) {
            return true;
        }
    }
    if (note[0][0] == note[1][1] && note[1][1] == note[2][2] && note[2][2] == note[3][3] && note[3][3] == ch) {
        return true;
    }
    if (note[0][3] == note[1][2] && note[1][2] == note[2][1] && note[2][1] == note[3][0] && note[3][0] == ch) {
        return true;
    }
    for (int i = 0; i < vex.size(); i++) {
        note[vex[i].first][vex[i].second] = 'T';
    }
    return false;
}

int main() {
    int T, cas = 1;
    scanf("%d", &T);
    while (T--) {
        for (int i = 0; i < 4; i++)
            scanf("%s", &note[i]);
        bool draw = false;
        int won[2] = {0}, cnt = 0;;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (note[i][j] == '.') {
                    cnt++;
                }
            }
        }
        if (judge('X')) won[0] = 1;
        if (judge('O')) won[1] = 1;
        if ((won[0] == won[1]) && cnt == 0) {
            draw = true;
        }
        if (draw) {
            printf("Case #%d: Draw\n", cas++);
        } else if (won[0]) {
            printf("Case #%d: X won\n", cas++);
        } else if (won[1]) {
            printf("Case #%d: O won\n", cas++);
        } else {
            printf("Case #%d: Game has not completed\n", cas++);
        }
    }
    return 0;
}