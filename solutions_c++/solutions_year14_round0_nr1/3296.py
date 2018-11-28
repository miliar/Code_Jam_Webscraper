#include <stdio.h>

main()
{
    int i, j, k;
    int card[2][4][4], t, a1, a2, counter, answer;
    scanf("%d", &t);
    for(i=1; i<=t; i++)
    {
        scanf("%d", &a1);
        for(j=0; j<=3; j++) for(k=0; k<=3; k++) scanf("%d", &card[0][j][k]);
        scanf("%d", &a2);
        for(j=0; j<=3; j++) for(k=0; k<=3; k++) scanf("%d", &card[1][j][k]);
        counter = answer = 0;
        a1--;
        a2--;
        for(j=0; j<=3; j++)
        {
            for(k=0; k<=3; k++)
            {
                if(card[0][a1][j] == card[1][a2][k])
                {
                    counter++;
                    if(counter == 1) answer = card[0][a1][j];
                    else
                    {
                        answer = -1;
                        break;
                    }
                }
            }
            if(answer == -1) break;
        }
        printf("Case #%d: ", i);
        if(answer == 0) printf("Volunteer cheated!\n");
        else if(answer == -1) printf("Bad magician!\n");
        else printf("%d\n", answer);
    }
}
