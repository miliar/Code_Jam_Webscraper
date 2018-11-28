#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1002

int main(void)
{
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        static char buffer [MAX];
        static int maxShy;
        int neededFriends = 0;;
        int totalOvation = 0;;
        scanf("%d %s", &maxShy, buffer);
        for (int i = 0; i <= maxShy; i++) {
            if (totalOvation < i)
            {
                neededFriends += i - totalOvation;
                totalOvation = i;
            }
            totalOvation += buffer[i] - '0';
        }
        printf("Case #%d: %d\n", tc, neededFriends);
    }
}
