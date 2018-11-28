#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>
#include <stdarg.h>
#include <fstream>

using namespace std;

char mas[100][100];
bool dang[100][100];

void solve(int t) {
    int r,c;
    cin>>r>>c;
    for (int i=0;i<r;i++) {
        for (int j=0;j<c;j++) {
            cin>>mas[i][j];
            dang[i][j]=false;
        }
    }
    int cnt=0;
    bool possible=true;
    for (int i=0;i<r;i++) {
        for (int j=0;j<c;j++) {
            bool danger=true;
            if (mas[i][j]=='.') {
                danger=false;
            } else if (mas[i][j]=='<') {   
                for (int k=j-1;k>=0;k--) {
                    if (mas[i][k]!='.') {
                        danger=false;
                        break;
                    }
                }
            } else if (mas[i][j]=='>') {
                for (int k=j+1;k<c;k++) {
                    if (mas[i][k]!='.') {
                        danger=false;
                        break;
                    }
                }
            } else if (mas[i][j]=='^') {
                for (int k=i-1;k>=0;k--) {
                    if (mas[k][j]!='.') {
                        danger=false;
                        break;
                    }
                }
            } else if (mas[i][j]=='v') {
                for (int k=i+1;k<r;k++) {
                    if (mas[k][j]!='.') {
                        danger=false;
                        break;
                    }
                }
            }
            if (danger) {
                cnt++;
                bool newDanger=true;
                for (int k=j-1;k>=0;k--) {
                    if (mas[i][k]!='.') {
                        newDanger=false;
                        break;
                    }
                }
                for (int k=j+1;k<c;k++) {
                    if (mas[i][k]!='.') {
                        newDanger=false;
                        break;
                    }
                }
                for (int k=i-1;k>=0;k--) {
                    if (mas[k][j]!='.') {
                        newDanger=false;
                        break;
                    }
                }
                for (int k=i+1;k<r;k++) {
                    if (mas[k][j]!='.') {
                        newDanger=false;
                        break;
                    }
                }
                if (newDanger) {
                    possible=false;
                    break;
                }
            }
        }
    }
    if (!possible) {
        printf("Case #%d: IMPOSSIBLE\n",t);
    } else {
        printf("Case #%d: %d\n",t,cnt);
    }
}

int main() {
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    cin>>t;
    for (int i=0;i<t;i++)
        solve(i+1);
    return 0;
}