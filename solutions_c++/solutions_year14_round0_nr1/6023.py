#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
using namespace std;


int main(void) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    bool marked[17];
    int _case, row, num, count, result;
    scanf("%d", &_case);
    for (int i = 1; i <= _case; i++) {
        // init
        count = 0;
        for (int j = 0; j <= 16; j++)
            marked[j] = false;
        // round 1
        scanf("%d", &row);
        for (int j = 1; j <= 4; j++) {
            for (int k = 1; k <= 4; k++) {
                scanf("%d", &num);
                if (j == row)
                    marked[num] = true;
            }
        }
        // round 2
        scanf("%d", &row);
        for (int j = 1; j <= 4; j++) {
            for (int k = 1; k <= 4; k++) {
                scanf("%d", &num);
                if (j == row && marked[num]){
                    result = num;
                    count++;
                }
            }
        }
        if(count == 1)
            printf("Case #%d: %d\n", i, result);
        else if(count > 1)
            printf("Case #%d: Bad magician!\n", i);
        else
            printf("Case #%d: Volunteer cheated!\n", i);
    }
    return 0;
}
