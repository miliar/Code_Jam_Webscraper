#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <list>
using namespace std;
int grid[4][4], row1, row2, cards, cheat, ans;
vector<int> first;
vector<int> second;
int main()
{
    int test, times=1;
    scanf("%d", &test);
    while(test--){
        cards=0, cheat=1, ans=0;
        first.clear(), second.clear();
        memset(grid, 0, sizeof(grid));
        scanf("%d", &row1);
        for(int i=0 ; i<4 ; i++)
            for(int j=0 ; j<4 ; j++)
                scanf("%d", &grid[i][j]);
        for(int i=0 ; i<4 ; i++)
            first.push_back(grid[row1-1][i]);
        sort(first.begin(), first.end());

        scanf("%d", &row2);
        for(int i=0 ; i<4 ; i++)
            for(int j=0 ; j<4 ; j++)
                scanf("%d", &grid[i][j]);
        for(int i=0 ; i<4 ; i++)
            second.push_back(grid[row2-1][i]);
        sort(second.begin(), second.end());

        for(int i=0 ; i<4 ; i++){
            for(int j=0 ; j<4 ; j++){
                if(first[i]==second[j])
                    ans = first[i], ++cards, cheat=0;
                if(cards>1)
                    break;
            }
            if(cards>1)
                    break;
        }
        if(cards==1)
            printf("Case #%d: %d\n", times++, ans);
        else if(cheat)
            printf("Case #%d: Volunteer cheated!\n", times++);
        else if(cards>=2)
            printf("Case #%d: Bad magician!\n", times++);
    }
    return 0;
}
