#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <cstdlib>
#include <ctime>
using namespace std;
int n;
char s[6][6];
int a[5][5], b[5][5];
int main() {
    int T;
    int cas = 0;
    srand(time(0));
    cin >> T;
    while(T--) {
        cin >> n;
        for(int i = 0; i < n; i++) {
            cin >>  s[i];
            for(int j = 0; j < n; j++) {
                a[i][j] = s[i][j] - '0';
            }
        }
        int f = n * n;
        int ans = -1;
        for(int i = 0; i < (1 << f); i++) {
            for(int j = 0; j < n; j++) {
                for(int k = 0; k < n; k++) b[j][k] = a[j][k];
            }
            int tt = 0;
            int fg = 0;
            for(int j = 0; j < f; j++) {
                if( i & (1 << j)) {
                    tt++;
                    int k = j / n;
                    int m = j % n;
                    if (a[k][m] == 1) fg = 1;

                    b[k][m] = (a[k][m]^1);
                }
            }
            if(fg) continue;
            int c[5]; 
            for(int j = 0; j < n; j++) c[j] = j;
            int flag = 1;
            //if (tt == 1) {
            //    for(int j =0 ; j < n; j++) {
            //        for(int k  = 0; k < n; k++) cout << "123 " << b[j][k] << endl;
            //    }
            //}
            do {
                if(flag == 0) break;
                for(int j = 0; j < 1000; j++) {
                    int ok[5]; 
                    if(flag == 0) break;
                    for(int k = 0;k < n; k++) ok[k] = 1;
                    for(int k = 0; k < n; k++) {
                        int cnt = 0;
                        for(int m = 0; m < n; m++) {
                            if(b[c[k]][m] == 1 && ok[m] == 1) cnt++;
                        }
                        if(cnt == 0) {
                            flag = 0;
                            break;
                        }
                        int z = rand()% cnt;
                        cnt = 0;
                        for(int m = 0; m < n; m++) {
                            if(b[c[k]][m] == 1 && ok[m] == 1) {
                                if(cnt == z) {
                                    ok[m] = 0;
                                    break;
                                }
                                cnt++;
                            }
                        }
                    }
                }
            }while(next_permutation(c, c + n));
            if (flag) {
                if(ans == -1) ans = tt;
                else ans = min(ans, tt);
            }
        }
        printf("Case #%d: %d\n", ++ cas, ans);
    }

    return 0;
}
