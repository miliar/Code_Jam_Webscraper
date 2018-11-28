
#include <string>
#include <iostream>
#include <cstdio>

int getMatchedNumbersCount(int prevNums[4], int currNums[4]) {
    int count = 0;
    
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            if (prevNums[i] == currNums[j])
                count++;
        }
    }
    
    return count;
}

int getMatchedNumber(int prevNums[4], int currNums[4]) {
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            if (prevNums[i] == currNums[j])
                return prevNums[i];
        }
    }
    return 0;
}

int main(int argc, const char * argv[])
{
    int T;
    scanf("%d", &T);
    
    int prevNums[4];
    int grid[4][4];
    
    for(int i=0; i<T; i++)
    {
        for (int j=0; j<2; j++) {
            int row;
            scanf("%d", &row);
            row--;
            
            for (int k=0; k<4; k++)
                scanf("%d %d %d %d", &grid[k][0], &grid[k][1], &grid[k][2], &grid[k][3]);
            
            // First run
            if (j==0) {
                for (int l=0; l < 4; l++)
                    prevNums[l] = grid[row][l];
            }
            
            // Second run
            else {
                printf("Case #%d: ", i+1);
                int selectedCards = getMatchedNumbersCount(prevNums, grid[row]);
                
                if (selectedCards == 0)
                    printf("Volunteer cheated!");
                else if (selectedCards == 1)
                    printf("%d", getMatchedNumber(prevNums, grid[row]));
                else
                    printf("Bad magician!");
                
                printf("\n");
            }
        }
    }
    
    return 0;
}
