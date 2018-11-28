#include <stdio.h>
#include <iostream>
#include <vector>
#include <string.h>


int main()
{
    using namespace std;
    int testcases;
    scanf("%d", &testcases);

    char arr[1020];
    int maxShyness;
    int total;
    int missingPeople;
    int j = 1;

    for (int i = 0; i < testcases; i ++)
    {
        memset (arr, 0, sizeof(arr));
        scanf("%d", &maxShyness);
        scanf("%s", arr);

        total = arr[0] - '0';
        missingPeople = (total == 0 ? 1 : 0);
        total += missingPeople;

        for(j = 1; j <= maxShyness; j ++)
        {
            if (total < j)
            {
                int currentMissing = j - total;
                total += currentMissing;
                missingPeople += currentMissing;
            }
            total += arr[j] - '0';
        }

        printf("Case #%d: %d\n", i + 1, missingPeople);
    }
    return 0;
}
