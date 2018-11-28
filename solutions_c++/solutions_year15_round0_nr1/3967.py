#include <stdio.h>

int main()
{
    int num;
    char line[1024];
    scanf("%d\n", &num);
    for(int i = 0; i < num; i++)
    {
        int Smax;
        scanf("%d ", &Smax);
        int total = 0;
        int nbToAdd = 0;
        scanf("%s", line);
        for(int j = 0; j <= Smax; j++)
        {
            char c = line[j];
            c -= '0';
            if(c > 0 && total < j)
            {
                nbToAdd += j-total;
                total = j;
            }
            total += c;
        }
        printf("Case #%d: %d\n", i+1, nbToAdd);
    }
    return 0;
}
