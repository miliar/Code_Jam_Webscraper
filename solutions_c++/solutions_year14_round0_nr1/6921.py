#include <stdio.h>
#include <set>
#include <vector>
#include <iostream>
using namespace std;

int mat[5][5];
int main() {
    int test;
    int row1, row2;
    scanf("%d",&test);
    for (int cas = 1; cas <= test; ++cas) {
        scanf("%d", &row1);
        row1--;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                cin >> mat[i][j];

        set<int> set1, set2;
        vector<int> vec1;
        for (int j = 0; j < 4; ++j)
            vec1.push_back(mat[row1][j]);
        
        scanf("%d", &row2);
        row2--;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                cin >> mat[i][j];

        for (int j = 0; j < 4; ++j)
            set2.insert(mat[row2][j]);
        
        std::vector<int> both;
        for (int i = 0; i < vec1.size(); ++i)
        if (set2.find(vec1[i]) != set2.end()) {
            both.push_back(vec1[i]);
        }

        printf("Case #%d: ", cas);
        if (both.size() == 1)
            printf("%d\n",both[0]);
        else if (both.size() > 1)
            printf("Bad magician!\n");
        else
            printf("Volunteer cheated!\n");
    }
}