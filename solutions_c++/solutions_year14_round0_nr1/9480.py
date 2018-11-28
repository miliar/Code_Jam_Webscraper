#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int deck1[4][4];
int deck2[4][4];
char ostr[100][100];

int isMatch(int r1, int r2) {
    int cnt = 0;
    int vCard = -1;
    for(int j = 0; j < 4; ++j) {
        int val = deck1[r1][j];
        for(int k = 0; k < 4; ++k) {
            if(val == deck2[r2][k]) {
                ++cnt;
                vCard = val;
            }
        }
    }
    if(cnt > 1) {
        return 0;
    }
    else if(cnt == 1) {
        return vCard;
    }
    else {
        return -1;
    }
}


int main() {

    int numDataSets, r1, r2;
    cin >> numDataSets;
    for(int iSet = 0; iSet < numDataSets; ++iSet) {
        cin >> r1;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                cin >> deck1[i][j];
            }
        }
        cin >> r2;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                cin >> deck2[i][j];
            }
        }
        int v = isMatch(r1 - 1, r2 - 1);
        if(v == 0) {
            printf("Case #%d: Bad Magician!\n", iSet + 1);
        }
        else if(v == -1) {
            printf("Case #%d: Volunteer cheated!\n", iSet + 1);
        }
        else {
            printf("Case #%d: %d\n", iSet + 1, v);
        }
    }
    return 0;
}
