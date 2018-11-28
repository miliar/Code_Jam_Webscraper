#include <string>
#include <cstdio>
#include <iostream>
#include <sstream>
using namespace std;

string solve(int grid1[4][4], int grid2[4][4], int r1, int r2) {
    /*
    printf("r1 = %d, r2 = %d\n", r1, r2);
    printf("grid1:\n");
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            cout << grid1[i][j];
            cout << " ";
        }
        cout << endl;
    }
    printf("grid2:\n");
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            cout << grid2[i][j];
            cout << " ";
        }
        cout << endl;
    }
    */
    int hash[17];
    int solution = -1;
    int v = -1;
    for(int i = 0; i < 17; i++) {
        hash[i] = 0;
    }

    for(int i=0; i < 4; i++) {
        hash[grid1[r1-1][i]] = 1;
    }

    for(int i=0; i < 4; i++) {
        if(hash[grid2[r2-1][i]] == 1) {
            solution++;
            v = grid2[r2-1][i];
        }
    }

    if(solution == -1) {
        return "Volunteer cheated!";
    } else if (solution == 0) {
        return to_string(v);
    } else {
        return "Bad magician!";
    }

}

int main()
{
    int T, n, r1, r2;
    int grid1[4][4];
    int grid2[4][4];
    string line;
    getline(cin, line);
    istringstream(line) >> T;

    for(int t = 1; t <= T; t++) {
        scanf("%d", &r1);
        for(int i = 0; i < 4; i++) {
            scanf("%d%d%d%d", grid1[i], grid1[i]+1, grid1[i]+2, grid1[i]+3);
        }
        scanf("%d", &r2);
        for(int i = 0; i < 4; i++) {
            scanf("%d%d%d%d", grid2[i], grid2[i]+1, grid2[i]+2, grid2[i]+3);
        }

        string res = solve(grid1, grid2, r1, r2);
        printf("Case #%d: %s\n", t, res.c_str());
    }


}
