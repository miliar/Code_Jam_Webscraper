#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
#include<bitset>
using namespace std;

const int N = 110;
const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};

char a[N][N];
int r, c;

void sol() {
    int i, j, k, px, py;

    cin >> r >> c;

    for(i = 1; i <= r; ++i) {
        cin >> (a[i] + 1);

        for(j = 1; j <= c; ++j) {

            if(a[i][j] == '^')
                a[i][j] = 3;
            if(a[i][j] == '.')
                a[i][j] = 6;
            if(a[i][j] == '>')
                a[i][j] = 0;
            if(a[i][j] == 'v')
                a[i][j] = 1;
            if(a[i][j] == '<')
                a[i][j] = 2;
        }
    }

    int rez = 0;

    for(i = 1; i <= r; ++i)
        for(j = 1; j <= c; ++j) if(a[i][j] != 6) {

            int vee = 0;

            px = i; py = j;
            while(px && py && px <= r && py <= c) {
                px += dx[ a[i][j] ];
                py += dy[ a[i][j] ];

                if(px && py && px <= r && py <= c && a[px][py] != 6) {
                    vee = 1;
                    break;
                }
            }

            if(vee)
                continue;

            for(k = 0; k < 4; ++k) {

                px = i;
                py = j;

                while(px && py && px <= r && py <= c) {
                    px += dx[ k ];
                    py += dy[ k ];

                    if(px && py && px <= r && py <= c && a[px][py] != 6) {
                        a[i][j] = k;
                        vee = 1;
                        break;
                    }
                }

                if(vee) {
                    ++rez;
                    break;
                }
            }

            if(!vee) {
                cout << "IMPOSSIBLE";
                return;
            }
        }

    cout << rez;
}

int main() {
    freopen("ttt", "r", stdin);
    freopen("tttt", "w", stdout);

    int t, a = 0;
    cin >> t;

    while(t--) {
        ++a;
        cout << "Case #" << a << ": ";
        sol();
        cout << "\n";
    }

    return 0;
}
