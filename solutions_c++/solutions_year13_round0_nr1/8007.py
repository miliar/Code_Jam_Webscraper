
#include <stdio.h>
#include <assert.h>

int main()
{
    char pad[5][5];
    char cross[2];
    int N = 0;
    int currentCase = 0;

    scanf("%d\n", &N);

    for (currentCase = 0; currentCase < N; currentCase++)
    {
        int lp, lpx, lpy;
        char tpx, tpy;
        char lineBuffer[10];
        char winner = 'D';
        bool dotExists = false;

        for (lp = 0; lp < 4; lp++)
        {
            scanf("%9s", lineBuffer);
            pad[lp][0] = lineBuffer[0];
            pad[lp][1] = lineBuffer[1];
            pad[lp][2] = lineBuffer[2];
            pad[lp][3] = lineBuffer[3];
            pad[lp][4] = 0;
        }

        pad[4][0] = pad[4][1] = pad[4][2] = pad[4][3] = pad[4][4] = 0;
        cross[0] = cross[1] = 0;

        for (lpy = 0; lpy < 4; lpy++)
        {
            for (lpx = 0; lpx < 4; lpx++)
            {
                int inc = 0;

                switch (pad[lpy][lpx])
                {
                    case 'O': inc = 10; break;
                    case 'X': inc = -10;break;
                    case 'T': 
                              tpx = lpx;
                              tpy = lpy;
                              break;
                    case '.': dotExists = true; break;
                    default: break;
                }

                pad[lpy][4] += inc;
                pad[4][lpx] += inc;
                if (lpy == lpx)       cross[0] += inc;
                if ((3 - lpy) == lpx) cross[1] += inc;
            }
        }

        if (pad[tpy][4] > 0) pad[tpy][4] += 10;
        if (pad[tpy][4] < 0) pad[tpy][4] -= 10;
        if (pad[4][tpx] > 0) pad[4][tpx] += 10;
        if (pad[4][tpx] < 0) pad[4][tpx] -= 10;
        if (tpx == tpy)
        {
            if (cross[0] > 0) cross[0] += 10;
            if (cross[0] < 0) cross[0] -= 10;
        }
        if ((3 - tpy) == tpx)
        {
            if (cross[1] > 0) cross[1] += 10;
            if (cross[1] < 0) cross[1] -= 10;
        }

        for (lp = 0; lp < 4; lp++)
        {
            if (pad[lp][4] >= 40)       winner = 'O';
            else if (pad[lp][4] <= -40) winner = 'X';
            else if (pad[4][lp] >= 40)  winner = 'O';
            else if (pad[4][lp] <= -40) winner = 'X';
            else if (cross[0] >= 40)    winner = 'O';
            else if (cross[0] <= -40)   winner = 'X';
            else if (cross[1] >= 40)    winner = 'O';
            else if (cross[1] <= -40)   winner = 'X';
        }

        //for (lpy = 0; lpy < 4; lpy++)
        //    printf("%2c %2c %2c %2c\t%d\n", pad[lpy][0], pad[lpy][1], pad[lpy][2], pad[lpy][3], pad[lpy][4]);
        //printf("%d %d %d %d\t(%d, %d)\n", pad[4][lpx], pad[4][lpx], pad[4][lpx], pad[4][lpx], cross[0], cross[1]);

        printf("Case #%d: ", currentCase + 1);
        switch (winner)
        {
            case 'O': printf("O won\n"); break;
            case 'X': printf("X won\n"); break;
            case 'D':
                      if (dotExists == true) printf("Game has not completed\n");
                      else
                          printf("Draw\n"); break;
            default:
                      assert(winner == 0);
                      break;
        }
    }

    return 0;
}







