#include <stdio.h>
#include <memory.h>


int answer;

int cards[4][4];

bool isCandidate[17];


void Input(void)
{
    scanf("%d", &answer);

    for(int i=0;i<4;i++)
        for (int j=0;j<4;j++)
            scanf("%d", &cards[i][j]);
}


int main()
{
    int casen;

    scanf("%d",&casen);

    for(int i=0;i<casen;i++)
    {
        memset(&cards, 0, sizeof(cards));
        memset( &isCandidate , 0 , sizeof( isCandidate ) );
        // First answer
        Input();

        for(int j=0;j<4;j++)
            isCandidate[  cards[answer-1][j] ] = true;

        // Second answer
        Input();

        int cnt = 0;
        int result = 0 ;

        for(int j=0;j<4;j++)
        {
            if ( isCandidate[ cards[answer-1][j]] )
            {
                result = cards[answer-1][j]; 
                cnt ++;
            }
        }

        printf("Case #%d: ",i+1);

        if ( cnt == 1 )
            printf("%d\n", result );
        else if ( cnt == 0 )
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
    }
    return 0;
}
