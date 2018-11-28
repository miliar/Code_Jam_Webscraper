#include <stdio.h>
#include <cstdlib>

using namespace std;

int main()
{
    char plat[1200];
    int maximum, num;

    scanf("%d\n", &num);
    for(int i = 0; i < num ; i++)
    {
        int minimum = 0;
        scanf("%d  %s", &maximum, plat);

        for(int j = 0; j <= maximum ; j++)
        {
            int pessoas = 0;
            for(int k = 0; k < j; k++)
            {
                pessoas += plat[k] - '0';
            }
            while(j > pessoas + minimum)
            {
                minimum++;
            }
        }
        printf("Case #%d: %d\n",i+1,minimum);
    }

    return 0;
}
