#include <iostream>
#include <cstdio>

using namespace std;

int T;
int grid1[4][4];
int grid2[4][4];

int solve(int n) {
    // input
    int first_ans, second_ans;
    cin >> first_ans;
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            cin >> grid1[i][j];
        }
    }
    cin >> second_ans;
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            cin >> grid2[i][j];
        }
    }

    // check
    int c = 0;
    int ans = 0;
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            if(grid1[first_ans-1][i] == grid2[second_ans-1][j]) {
                c += 1;
                ans = grid1[first_ans-1][i];
            }
        }
    }

    if(c == 0) {
        printf("Case #%d: Volunteer cheated!\n", n+1);
    } else if(c == 1) {
        printf("Case #%d: %d\n", n+1, ans);
    } else {
        printf("Case #%d: Bad magician!\n", n+1);
    }

    return 0;
}

int main() {
    cin >> T;
    for(int i = 0; i < T; i++) {
        solve(i);
    }
    return 0;
}
