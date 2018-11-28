#include <stdio.h>

int main ()
{
    int T, first, last, chosen;
    int cards[4][4], possible[4];
    bool bad;
    scanf("%d", &T);
    for (int t = 0; t < T; ++t)
    {
        chosen = 0;
        bad = false;

        // Prepare first arrange
        scanf("%d", &first);
        first--;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                scanf("%d", &cards[i][j]);
            }
        }

        // Determine possible chosen
        for (int i = 0; i < 4; ++i)
        {
            possible[i] = cards[first][i];
        }

        // Prepare second arrange
        scanf("%d", &last);
        last--;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                scanf("%d", &cards[i][j]);
            }
        }

        // Determine the card
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                if (cards[last][j] == possible[i])
                {
                    if (chosen != 0)
                    {
                        bad = true;
                    }
                    chosen = possible[i];
                }
            }
        }

        // Print the result
        printf("Case #%d: ", t+1);
        if (bad)
        {
            printf("Bad magician!\n");
        }
        else if (chosen != 0)
        {
            printf("%d\n", chosen);
        }
        else
        {
            printf("Volunteer cheated!\n");
        }
    }
}