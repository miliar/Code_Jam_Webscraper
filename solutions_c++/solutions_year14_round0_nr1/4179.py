#include <stdio.h>
#include <math.h>
#include <sched.h>

int main()
{
    struct sched_param param;
    param.sched_priority = 99;
    sched_setscheduler(0, SCHED_FIFO, &param);

    int rows[2][4];
 
    int dummy;
    
    int T;
    scanf("%d", &T);
    long double C;
    long double F;
    long double X;
    
    int selected = 0;
    for (int i=0;i<T;++i)
    {
        scanf("%d", &selected);

        for (int j=0;j<4;++j)
        {
            if (j+1==selected)
            {
                scanf("%d %d %d %d", &rows[0][0], &rows[0][1], &rows[0][2], &rows[0][3]);
            }
            else
            {
                scanf("%d %d %d %d", &dummy, &dummy, &dummy, &dummy);
            }
        }

        scanf("%d", &selected);
        for (int j=0;j<4;++j)
        {
            if (j+1==selected)
            {
                scanf("%d %d %d %d", &rows[1][0], &rows[1][1], &rows[1][2], &rows[1][3]);
            }
            else
            {
                scanf("%d %d %d %d", &dummy, &dummy, &dummy, &dummy);
            }
        }

        
        int matched = 0;
        int card = 0;
        for (int k=0;k<4;++k)
        {
            for (int j=0;j<4;j++)
            {
                if (rows[0][k] == rows[1][j])
                {
                    matched++;
                    card = rows[0][k];
                }
            }
        }
        
        if (matched==1)
        {
            printf("Case #%d: %d\n", i+1, card);
        }
        else if (matched==0)
        {
            printf("Case #%d: Volunteer cheated!\n", i+1);
        }
        else 
        {
            printf("Case #%d: Bad magician!\n", i+1);
        }
    }
}
