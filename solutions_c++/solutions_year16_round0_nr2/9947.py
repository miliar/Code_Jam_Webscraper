#include <cstdio>
#include <cstring>
char cStr[105];

int main ()
{
    int T, caseCount = 0, result, cStrLen;
    char chPrev;
    scanf("%d", &T);
    while (T--) {
        scanf("%s", cStr);
        cStrLen = strlen(cStr);

        chPrev = cStr[0];
        if (chPrev == '+')
            result = 0;
        else
            result = 1;

        for (int i = 1; i < cStrLen; ++i)
        {
            if (chPrev == '+' && cStr[i] == '-')
                result += 2;
            chPrev = cStr[i];
        }
        printf("Case #%d: %d\n", ++caseCount, result);
    }
    return 0;
}
