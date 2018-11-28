#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

#define debug 01
#define openfile {freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);}

const int MaxN = 20;
const string b[2] = {"Bad magician!","Volunteer cheated!"};

int a[MaxN][MaxN];
bool f[MaxN];

int n, t, te;

void readfile_and_solve() {
    int r, nho, dem = 0;
    scanf("%d",&r);
    for (int i = 1; i <= 4; ++i) {
        for (int j = 1; j<= 4; ++j) scanf("%d",&a[i][j]);
        if (i == r)
            for (int j = 1; j<=4; ++j) f[a[i][j]] = 1;
    }
    scanf("%d",&r);
    for (int i = 1; i<= 4; ++i) {
        for (int j = 1; j<= 4; ++j) scanf("%d",&a[i][j]);
        if (i == r)
            for (int j = 1; j<=4; ++j) {
                dem += f[a[i][j]];
                if (f[a[i][j]] == 1) nho = a[i][j];
            }
    }
    if (dem == 0) {
        cout << b[1] << "\n";
        return;
    }
    if (dem != 1) {
        cout << b[0] << "\n";
        return;
    }
    printf("%d\n",nho);
}

void reset_memory() {
    memset(f,0,sizeof f);
}

int main() {
    if (debug) openfile;
    scanf("%d",&t);
    for (int te = 1; te <= t; ++te) {
        printf("Case #%d: ",te);
        readfile_and_solve();
        reset_memory();
    }
}
