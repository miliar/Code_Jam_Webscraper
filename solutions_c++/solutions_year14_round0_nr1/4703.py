#include<iostream>
#include<vector>
#include<cstdio>
#include<set>
#include<map>
#include<algorithm>
#include<string.h>
#include<string>
#include<cassert>
#include<stack>
#include<queue>
#include<cmath>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int, int> PI;

int main() {
    int t;
    int f, s, cnt, val;
    int grid1[4][4];
    int grid2[4][4];

    scanf("%d", &t);

    for(int tt = 1; tt <= t; tt++) {
        cnt = 0;
        scanf("%d", &f);
        f--;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                scanf("%d", &grid1[i][j]);
            }
        }

        scanf("%d", &s);
        s--;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                scanf("%d", &grid2[i][j]);
            }
        }

        for(int i = 0; i < 4; i++) {
            // check if grid1[f][i] is present in the grid2[s][] or not.
            for(int j = 0; j < 4; j++) {
                if(grid1[f][i] == grid2[s][j]) {
                    val = grid1[f][i];
                    cnt++;
                }
            }
        }
        //printf("%d", cnt);
        printf("Case #%d: ", tt);
        if(cnt == 0) printf("Volunteer cheated!\n");
        if(cnt == 1) printf("%d\n", val);
        if(cnt > 1) printf("Bad magician!\n");
    }

}
