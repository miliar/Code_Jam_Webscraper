#include <cstdio>

int main() {
    int T, TT;
    scanf("%d", &TT);
    
    for (T = 1; T <= TT; T++) {
        
        printf("Case #%d: ", T);
        int used[17] = {0};
        int grid[4][4];
        
        int i, j;
        
        int row;
        scanf("%d", &row);
        
        
        for (i = 0; i < 4; i++)
            for (j = 0; j < 4; j++)
                scanf("%d", &grid[i][j]);
        
        for (i = 0; i < 4; i++)
            used[grid[row-1][i]] = 1;
        
        int ans = 0;
        
        scanf("%d", &row);
        
        for (i = 0; i < 4; i++)
            for (j = 0; j < 4; j++)
                scanf("%d", &grid[i][j]);
        
        
        for (i = 0; i < 4; i++) {
            if (used[grid[row-1][i]] && ans)
                ans = -1;
            else if (used[grid[row-1][i]])
                ans = grid[row-1][i];
        }
        
        if (ans == 0)
            printf("Volunteer cheated!\n");
        else if (ans == -1)
            printf("Bad magician!\n");
        else
          printf("%d\n", ans);
      
    }
}
        