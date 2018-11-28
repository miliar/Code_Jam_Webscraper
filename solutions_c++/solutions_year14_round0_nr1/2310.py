#include <cstdio>
#include <assert.h>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

#define foreach(it, s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define X first
#define Y second

const int MAX_N = 100001;
const int MAX_M = 100001;
const int MOD = 1e9 + 7.5;
const double EPS = 1e-8;

int a[8][8], b[8][8];

void solve(int ca){
    int r1, r2;
    cin >> r1;
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++){
            cin >> a[i][j];
        }
    }
    cin >> r2;
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++){
            cin >> b[i][j];
        }
    }
    --r1, --r2;
    int cnt = 0, val;
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++) if (a[r1][i] == b[r2][j]) ++cnt, val = a[r1][i];
    }
    if (cnt == 1){
        printf("Case #%d: %d\n", ca, val);
    } else
    if (cnt > 1){
        printf("Case #%d: Bad magician!\n", ca);
        return;
    } else printf("Case #%d: Volunteer cheated!\n", ca);
}

int main(){
    int ca;
    cin >> ca;
    for (int i = 0; i < ca; i++){
        solve(i + 1);
    }
    return 0;
}
