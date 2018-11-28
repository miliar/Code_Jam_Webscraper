#include <cstdio>

using namespace std;

void LoadRow(int numsInRow[4])
{
    int row, temp;
    scanf("%d", &row);
    
    int cRow = 0;
    
    for (; cRow != row - 1; ++cRow)
    {
        for (int i = 0; i < 4; ++i)
            scanf("%d", &temp);
    }
    
    for (int i = 0; i < 4; ++i)
        scanf("%d", numsInRow + i);
        
    cRow += 1;
    
    for (; cRow < 4; ++cRow)
    {
        for (int i = 0; i < 4; ++i)
            scanf("%d", &temp);
    }
}

int main()
{
    int firstMatches[4], secondMatches[4], T;
    int match;
    
    scanf("%d", &T);
    
    for (int t = 1; t <= T; ++t)
    {
        LoadRow(firstMatches);
        LoadRow(secondMatches);
        
        match = 0;
        
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                if (firstMatches[i] == secondMatches[j])
                {
                    if (match == 0)
                        match = firstMatches[i];
                    else
                        match = -1;
                }
        
        if (match == -1)
            printf("Case #%d: Bad magician!\n", t);
        else if (match == 0)
            printf("Case #%d: Volunteer cheated!\n", t);
        else
            printf("Case #%d: %d\n", t, match);
    }
}