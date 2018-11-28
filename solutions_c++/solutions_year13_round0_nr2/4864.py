#include <string>
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string.h>
using namespace std;

int n, m;
int mtx[102][102];
bool judge(int ii, int jj){
    bool ok = true;
    for (int i = 0; i < n; i++)
        if (mtx[i][jj] > mtx[ii][jj]){
            ok = false;
            break;
        }
    if (ok)
        return ok;
    ok = true;
    for (int j = 0; j < m; j++)
        if (mtx[ii][j] > mtx[ii][jj]){
            ok = false;
            break;
        }
    return ok;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("out_lar", "w", stdout);
    int t;
    cin >> t;
    for (int cc = 1; cc <= t; cc++){
        cin >> n >> m;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++)
                cin >> mtx[i][j];
        }

        bool ok = true;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                    ok = judge(i, j);
                    if (!ok)
                        break;
            }
            if (!ok)
                break;
        }

        printf("Case #%d: %s\n", cc, (ok ? "YES" : "NO"));
    }

    return 0;
}
