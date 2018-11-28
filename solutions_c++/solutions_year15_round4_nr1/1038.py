#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cstdio>

using namespace std;
int r,c;
string matrix[101];
char change[101][101];
int cntr[101];
int cntc[101];

int solve() 
{
    cin>>r>>c;
    int i, j, k;
    //cout<<"====================="<<endl;
    for (i=0; i<r; i++) {
        cin>>matrix[i];
        //cout<<matrix[i]<<endl;
    }
    //cout<<"====================="<<endl;
    for (i=0; i<r; i++) {
        cntr[i] = 0;
        for (j=0; j<c; j++) {
            if (matrix[i][j]!='.')
                cntr[i]++;
        }
    }
    for (j=0; j<c; j++) {
        cntc[j] = 0;
        for (i=0; i<r; i++) {
            if (matrix[i][j]!='.')
                cntc[j]++;
        }
    }

    for (i=0; i<r; i++) {
        for (j=0; j<c; j++) {
            change[i][j] = matrix[i][j];
            if (matrix[i][j]=='<') {
                for (k=j-1; k>=0; k--) {
                    if (matrix[i][k] != '.') {
                        change[i][j] = '.';
                        break;
                    }
                }
            } else if (matrix[i][j]=='>') {
                for (k=j+1; k<c; k++) {
                    if (matrix[i][k] != '.') {
                        change[i][j] = '.';
                        break;
                    }
                }
            } else if (matrix[i][j]=='^') {
                for (k=i-1; k>=0; k--) {
                    if (matrix[k][j] != '.') {
                        change[i][j] = '.';
                        break;
                    }
                }
            } else if (matrix[i][j]=='v') {
                for (k=i+1; k<r; k++) {
                    if (matrix[k][j] != '.') {
                        change[i][j] = '.';
                        break;
                    }
                }
            }
        }
    }

    int poss = 1;
    int cnt = 0;

    for (i=0; i<r; i++) {
        for (j=0; j<c; j++) {
            if (change[i][j]!='.') {
                if (cntr[i]==1 && cntc[j]==1)
                    poss = 0;
                cnt++;
            }
        }
    }
    if (poss == 0)
        cout<<"IMPOSSIBLE"<<endl;
    else
        cout<<cnt<<endl;

    return 1;
}

int main() {
    int nc, tc;
    tc = 1;
    cin>>nc;
    while (tc<=nc) {
        cout<<"Case #"<<tc<<": ";
        solve();
        tc++;
    }
    return 0;
}
