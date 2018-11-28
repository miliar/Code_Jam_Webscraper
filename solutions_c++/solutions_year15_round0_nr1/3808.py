#include <iostream>
#include <stdio.h>
using namespace std;

const int MaxSMax = 1000;

int T;
int smax;
char s[MaxSMax+5];

int main()
{
    scanf("%d",&T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d",&smax);
        scanf("%s",s);

        int result = 0;
        int currentSum = 0;

        for (int i = 0; i <= smax; ++i) {

            if ( currentSum < i ) {
                result += i - currentSum;
                currentSum += i - currentSum;
            }

            currentSum += (s[i] - '0');
        }

        printf("Case #%d: %d\n", t, result);
    }

    return 0;
}
