#include <iostream>
#include <fstream>
#include <string>
#include <utility>
#include <stdio.h>
#include <string.h>
using namespace std;
char tmap[200][200];
int c[200][200];
int n,m;
int main() {
    freopen("input.in", "r", stdin); freopen("output.txt", "w", stdout);
    int cases;
    cin >> cases;
    for (int ccs = 1; ccs <= cases; ccs++) {
        //cout << "Test case #" << ccs << endl;
        int ans = 0;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) scanf("%s", &tmap[i][0]);
        //for (int i=0; i<n; i++) cout << tmap[i] << endl;
        memset(c, 0, sizeof(c));
        for (int i = 0; i < n; i++) {
            for (int j=0; j<m; j++) if (tmap[i][j] != '.') {
                if (tmap[i][j] == '<') { ans += 1; }
                c[i][j] += 1;
                break;
            }
            for (int j=m-1; j>=0; j--) if (tmap[i][j] != '.') {
                if (tmap[i][j] == '>') {  ans += 1; }
                c[i][j] += 1;
                break;
            }
        }
        for (int j = 0; j < m; j++) {
            for (int i=0; i<n; i++) if (tmap[i][j] != '.') {
                if (tmap[i][j] == '^') { ans += 1; }
                c[i][j] += 1;
                break;
            }
            for (int i=n-1; i>=0; i--) if (tmap[i][j] != '.') {
                if (tmap[i][j] == 'v') {ans += 1; }
                c[i][j] += 1;
                break;
            }

        } // j
        bool avl = 1;
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (c[i][j] == 4) avl = 0;
        if (avl) cout << "Case #" << ccs << ": " << ans << endl;
        else cout << "Case #" << ccs << ": IMPOSSIBLE" << endl;
    } // ccs
    //fclose(cin);fclose(cout);
}
