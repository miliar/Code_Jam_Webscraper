#include <stdio.h>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int N, R, P, S;

string f[13][3];

void init(){
        f[0][0] = 'P';
        f[0][1] = 'R';
        f[0][2] = 'S';

        for (int i = 1; i <= 12; i ++) {
                for (int j = 0; j < 3; j ++) {
                        string st1 = f[i-1][j] + f[i-1][(j + 1) % 3];
                        string st2 = f[i-1][(j + 1) % 3] + f[i-1][j];
                        f[i][j] = min(st1, st2);
                }
        }
}


int main(){
        freopen("a.in", "r", stdin);
        freopen("a.out", "w", stdout);

        init();

        int tt, ca = 0;
        scanf("%d", &tt);
        while (tt--) {
                printf("Case #%d: ", ++ca);
                cin >> N >> R >> P >> S;
                string ans = "Z";
                for (int i = 0; i < 3; i ++){
                        int p = 0, r = 0, s = 0;
                        int len = f[N][i].size();
                        for (int j = 0; j < len; j ++){
                                switch (f[N][i][j]){
                                        case 'P' : p ++; break;
                                        case 'R' : r ++; break;
                                        case 'S' : s ++; break;
                                }
                        }
                        if (p == P && r == R && s == S){
                                ans = min(ans, f[N][i]);
                        }
                }
                if (ans == "Z") cout << "IMPOSSIBLE" << endl;
                else cout << ans << endl;
        }
}
