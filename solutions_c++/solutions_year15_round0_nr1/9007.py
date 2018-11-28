#include <stdio.h>

int main()
{
    int testNumber, shyest, si, need, sum;

    scanf("%d", &testNumber);
    
    for (int n = 1; n <= testNumber; n++)
    {
        sum = 0;
        need = 0;
        scanf("%d", &shyest);
        
        //printf("shyest : %1d ", shyest);
        for(int i = 0; i < shyest+1; i++)
        {
            scanf("%1d", &si);
            //printf("i,si %d, %d\n", i, si);
            sum += si;

            if (sum <= i)
            {
                need++;
                sum++;
            }
        }
       
        printf("Case #%d: %d\n", n, need);
    }
    
    return 0;
}

