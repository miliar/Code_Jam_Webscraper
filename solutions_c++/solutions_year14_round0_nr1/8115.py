#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#define MAX_S 4
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
using namespace std;

int board1[MAX_S][MAX_S], board2[MAX_S][MAX_S];
vector<int> ans;

int main()
{
    int t, first_row, second_row, case_no = 1;;
    scanf("%d", &t);
    FOR(i, 0, t)
    {
        scanf("%d", &first_row);
        --first_row;
        FOR(i, 0, MAX_S)
            FOR(j, 0, MAX_S)
                scanf("%d", &board1[i][j]);

        scanf("%d", &second_row);
        --second_row;
        FOR(i, 0, MAX_S)
            FOR(j, 0, MAX_S)
                scanf("%d", &board2[i][j]);

        FOR(i, 0, MAX_S)
            FOR(j, 0, MAX_S)
                if(board2[second_row][j] == board1[first_row][i])
                    ans.push_back(board2[second_row][j]);
        if(ans.empty())
            printf("Case #%d: Volunteer cheated!\n", case_no);
        else if(ans.size() == 1)
            printf("Case #%d: %d\n", case_no, ans.front());
        else
            printf("Case #%d: Bad magician!\n", case_no);
        ++case_no;
        ans.clear();
    }
    return 0;
}
