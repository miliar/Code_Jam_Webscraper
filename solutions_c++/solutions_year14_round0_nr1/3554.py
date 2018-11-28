#include <iostream>
#include <cstdio>


int main()
{
    
    int cases, i, r, n1, n2, n3, n4;
    scanf("%d", &cases);
    for(int z=0; z<cases; z++)
    {
        int card[16] = {0};
        for(int k=0; k<2;k++)
        {
            scanf("%d", &r);
            for(i = 0; i<4; i++)
            {
                scanf("%d%d%d%d", &n1,&n2,&n3,&n4);
                if (r == i+1)
                {
                    card[n1-1]++;
                    card[n2-1]++;
                    card[n3-1]++;
                    card[n4-1]++;
                }
            }
        }
        int num2=0, ca = -1;
        for(i=0;i<16;i++)
        {
            if (card[i] == 2)
            {
                ca = i+1;
                num2++;
            }
            
        }
        
        
        printf("Case #%d: ", z+1);
        switch(num2)
        {
            case 0: printf("Volunteer cheated!\n"); break;
            case 1: printf("%d\n", ca); break;
            default: printf("Bad magician!\n"); break;
        }
    }
}
