#include <cstdio>
#include <math.h>
using namespace std;
int counter = 0;
void work() {
    printf("Case #%d: ", ++counter);
    int answer_a, answer_b;
    scanf("%d", &answer_a);
    int a, b, c, d;
    int grid_a[4][4];
    int grid_b[4][4];
    int noa = 0, posa = 0;
    
    for (int i = 0; i < 4; ++i) {
        scanf("%d %d %d %d", &grid_a[i][0], &grid_a[i][1], &grid_a[i][2], &grid_a[i][3]);
    }
    
    scanf("%d", &answer_b);
    
    for (int i = 0; i < 4; ++i) {
        scanf("%d %d %d %d", &grid_b[i][0], &grid_b[i][1], &grid_b[i][2], &grid_b[i][3]);
    }

    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if(grid_a[answer_a-1][i] == grid_b[answer_b-1][j]){
                noa++;
                posa = grid_a[answer_a-1][i];
            }
        }
    }
    if (noa == 0) printf("Volunteer cheated!\n");
    if (noa == 1) printf("%d\n", posa);
    if (noa > 1) printf("Bad magician!\n");
    return;
}

int main() {
    int t; scanf("%d", &t);
    while(t--) {
        work();
    }
    return 0;
}