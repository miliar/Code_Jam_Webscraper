#include <iostream>
#include "cstring"
#include "cstdio"
using namespace std;

int r1;
int r2;
int maze[5];
bool hash[17];
int main()
{
    freopen("C:\\Users\\XPX\\Desktop\\A-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\XPX\\Desktop\\out.txt","w",stdout);
    int T, cas = 0;
    int ans;
    cin >> T ;
    while (T--) {
            ans = 0;
            memset ( hash, false, sizeof(hash) );
            cin >> r1;
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                        cin >> maze[j];
                        if (i + 1== r1) {
                                hash[ maze[j] ] = true;
                        }
                }
            }
            cin >> r2;
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j ++) {
                        cin >> maze[j];
                        if (i + 1 == r2) {
                                if (hash[ maze[j] ]) {
                                        if (ans == 0) {
                                                ans = maze[j];//one
                                        }else if (ans > 0) {
                                                ans = -1;//mult
                                        }
                                }
                        }
                }
            }
            cout << "Case #" << (++cas) << ": " ;
            if (ans == -1) {
                    cout << "Bad magician!" << endl;
            }else if (ans == 0) {
                    cout << "Volunteer cheated!" << endl;
            }else {
                    cout << ans << endl;
            }
    }
    return 0;
}
