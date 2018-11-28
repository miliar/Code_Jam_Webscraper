#include <cstdio>
#include <cstdlib>
#include <cstring>
#define ARBLIMIT 100
using namespace std;

int main()
{
    int n, T, sLen, numGroups;
    char s[101];
    scanf("%d", &T);
    for(int t=1; t <= T; ++t)
    {
        scanf("%s", s);
        sLen = strlen(s);
        char curGroup = s[0];
        numGroups = 1;
        for(int i=1; i < sLen; ++i)
        {
            if(curGroup != s[i])
            {
                numGroups++;
                curGroup = s[i];
            }
        }

        if(curGroup == '+')
            numGroups--;

        printf("Case #%d: %d\n", t, numGroups);
    }

    return 0;
}
