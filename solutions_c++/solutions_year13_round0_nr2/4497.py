#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;
int rowmax[105][105];
int colmax[105][105];
int field[105][105][105];
int r[105];
int c[105];

int main() {
    if(fopen("lawn.in","r")) {
        freopen("lawn.in","r",stdin);
        freopen("lawn.out","w",stdout);
    }
    int t;
    cin >> t;
    for(int i=1; i<=t; i++) {
        cin >> r[i] >> c[i];
        for(int j=1; j<=r[i]; j++) {
            for(int k=1; k<=c[i]; k++) {
                cin >> field[i][j][k];
            }
        }
        for(int j=1; j<=r[i]; j++) {
            for(int k=1; k<=c[i]; k++) {
                rowmax[i][j] = max(rowmax[i][j],field[i][j][k]);
            }
        }
        for(int k=1; k<=c[i]; k++) {
            for(int j=1; j<=r[i]; j++) {
                colmax[i][k] = max(colmax[i][k],field[i][j][k]);
            }
        }
    }

    for(int i=1; i<=t; i++) {
        int newfield[105][105];
        for(int j=1; j<=r[i]; j++) {
            for(int k=1; k<=c[i]; k++) {
                newfield[j][k] = 100;
            }
        }
        for(int j=1; j<=r[i]; j++) {
            //if(field[i][j][1] >= rowmax[i][j]) {
                for(int k=1; k<=c[i]; k++) {
                    if(rowmax[i][j] < newfield[j][k]) newfield[j][k] = rowmax[i][j];
                }
            //}
        }

        for(int k=1; k<=c[i]; k++) {
            //if(field[i][1][k] >= colmax[i][k]) {
                for(int j=1; j<=r[i]; j++) {
                    if(colmax[i][k] < newfield[j][k]) newfield[j][k] = colmax[i][k];
                }
            //}
        }
        bool bad = false;
        for(int j=1; j<=r[i]; j++) {
            for(int k=1; k<=c[i]; k++) {
                if(field[i][j][k] != newfield[j][k] && !bad) {
                    cout << "Case #" << i << ": NO" << '\n';
                    bad = true;
                }
            }
        }
        if(!bad) {cout << "Case #" << i << ": YES" << '\n';}
    }
    return 0;
}
