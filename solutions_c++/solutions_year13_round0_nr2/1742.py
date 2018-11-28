#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
int n, m;
int mat[100][100];
bool isValid(int x, int y) {
    bool ok_row=true;
    bool ok_col=true;
    for(int i=0; i<m; i++) {
        if(mat[x][i] > mat[x][y]) {
            ok_row=false;
            break;
        }
    }
    for(int i=0; i<n; i++) {
        if(mat[i][y] > mat[x][y]) {
            ok_col = false;
            break;
        }
    }
    return (ok_row || ok_col);
}

int main() {
    freopen("inpB.txt","r",stdin);
    freopen("outB.txt","w",stdout);
    int t;
    cin >> t;

    for(int cases=1; cases<=t; cases++) {
        cin >> n >> m;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                cin >> mat[i][j];
            }
        }
        cout << "Case #" << cases <<": ";
        bool ok=true;
        for(int i=0; i<n; i++) {
            if(ok) {
                for(int j=0; j<m; j++) {
                    if(!isValid(i,j)) {
                        ok=false;
                        break;
                    }
                }
            }
        }
        (ok)?(cout << "YES\n"):(cout << "NO\n");

    }
}
