#include <iostream>
#include <cstdio>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>


#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define pii pair < int, int >


using namespace std;


typedef long long LL;


const int INF = 1e9;
const double EPS = 1e-6;


int main() {
    freopen("inp", "r", stdin);
    freopen("outp", "w", stdout);
    int t;
    cin >> t;

    map < char, int > mmp;
    mmp['^'] = 0;
    mmp['>'] = 1;
    mmp['v'] = 2;
    mmp['<'] = 3;
    //cout << t << endl;

    for (int q = 1; q <= t; ++q) {
        //cout << "lol" << endl;
        int ans = 0;
        int h, w;
        cin >> h >> w;
        char mat[h][w];
        
        string s;
        for (int i = 0; i < h; ++i) {
            cin >> s;
            //cout << s << endl;
            for (int j = 0; j < w; ++j) {
                mat[i][j] = s[j];
            }
        }

        

        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                int num = 4;
                if (mat[i][j] == '.') {
                    continue;
                }
                vector < bool > cnt (4, false);
                for (int k = i - 1; k >= 0; --k) {
                    if (mat[k][j] != '.') {
                        cnt[0] = true;
                        --num;
                        //cout << "cs0" << endl;
                        break;
                    }
                }

                for (int k = j + 1; k < w; ++k) {
                    if (mat[i][k] != '.') {
                        cnt[1] = true;
                        --num;
                        //cout << "cs1" << endl;
                        break;
                    }
                }

                for (int k = i + 1; k < h; ++k) {
                    if (mat[k][j] != '.') {
                        cnt[2] = true;
                        --num;
                        //cout << "cs2" << endl;
                        break;
                    }
                }
                for (int k = j - 1; k >= 0; --k) {
                    if (mat[i][k] != '.') {
                        cnt[3] = true;
                        --num;
                        //cout << "cs3" << endl;
                        break;
                    }
                }
                if (num == 4) {
                    ans = -1;
                    //cout << "#" << endl;
                    break;
                }

                int tp = mmp[mat[i][j]];
                if (!cnt[tp]) {
                    ++ans;
                }
            }
            if (ans == -1) {
                break;
            }
        }

        cout << "Case #" << q << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE";
        }
        else {
            cout << ans;
        }
        cout << endl;
    }
    return 0;
}