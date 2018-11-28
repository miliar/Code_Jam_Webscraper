#include <stdio.h>

int main(int argc, char** argv)
{
    int T;
    scanf("%d\n",&T);

    char line[1024];
    for(int t = 0; t < T; t++)
    {

        int shyCount;
        scanf("%d %s",&shyCount,line);
        shyCount++;
        int frCount = 0;
        int upCount = 0;

        for (int i = 0; i < shyCount; i++)
        {
            int p = line[i] - '0';
            int newFrCount = 0;
            if(upCount < i)
            {
                newFrCount = i - upCount;
                frCount += newFrCount;
            }
            upCount += p + newFrCount;
        }
        printf("Case #%d: %d\n",t+1,frCount);
    }
}