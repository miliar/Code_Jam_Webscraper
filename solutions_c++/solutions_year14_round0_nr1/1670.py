#include <stdio.h>

using namespace std;

int main()
{
    int cases;
    int cur_case;
    char line[81];
    scanf("%d",&cases);
    fgets(line,80, stdin);

    for(cur_case = 1; cur_case<=cases; cur_case++)
    {
        fgets(line,80,stdin);
        int row;
        int i;
        sscanf(line,"%d",&row);
        for(i =0; i<row; i++)
            fgets(line,80,stdin);
 
        int cards[4];
        //for( i=0; i<4; i++)
        sscanf(line,"%d %d %d %d\n",&cards[0],&cards[1],&cards[2],&cards[3]);
        
        for( ; i<=4; i++)
            fgets(line,80,stdin);
        
        sscanf(line,"%d",&row);
        for( i =0; i< row-1; i++)
            fgets(line,80,stdin);

        int count=0;
        int pick=0;
        for(int k = 0; k<4; k++)
        {
                
            int cur;
            scanf("%d",&cur);
            for(int j=0;j<4;j++)
            {
                    
                if(cur == cards[j])
                {
                    count++;
                    pick = cur;
                }
            }

        }
        for( ; i<4; i++)
            fgets(line,80,stdin);
        printf("Case #%d: ",cur_case);
        if(count == 0)
            printf("Volunteer cheated!\n");
        else if(count >1)
            printf("Bad magician!\n");
        else
            printf("%d\n",pick);
    }
    
    return 0;
}
