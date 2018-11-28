#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
using namespace std;
int a[5][5], b[5][5];

void solve() {
    int x, y;
    cin >> x;
    for (int i = 1; i <= 4; i++) 
        for (int j = 1; j <= 4; j++) cin >> a[i][j];
    cin >> y;
    for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++) cin >> b[i][j];
    

    int ans = 0, rans;
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) if (b[y][j] == a[x][i])
        {
            ans++;
            rans = a[x][i];
        }
    }

    

    if (ans == 1) {
        printf("%d\n", rans);
        return;
    }
    if (ans) printf("Bad magician!\n"); else printf("Volunteer cheated!\n");



}


int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
}
