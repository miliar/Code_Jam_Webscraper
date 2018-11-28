#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>

using namespace std;

int T, r1, r2, a1[4][4], a2[4][4];
int main() {
    ifstream f("magic_trick.txt");
    f >> T;
    int caseNumber = 1;
    while(T-- > 0) {
        f >> r1;
        r1--;
        for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            f >> a1[i][j];
        
        f >> r2;
        r2--;
        for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            f >> a2[i][j];

        vector<int> ret;

        for(int j1 = 0; j1 < 4; j1++) {
            for(int j2 = 0; j2 < 4; j2++) if (a1[r1][j1] == a2[r2][j2]) {
                ret.push_back(a1[r1][j1]);
                break;
            }
        }

        if (ret.size() == 0) {
            printf("Case #%d: Volunteer cheated!\n", caseNumber++);
        } else if (ret.size() > 1) {
            printf("Case #%d: Bad magician!\n", caseNumber++);
        } else {
            printf("Case #%d: %d\n", caseNumber++, ret[0]);
        }   
        
    }
    return 0;
}
