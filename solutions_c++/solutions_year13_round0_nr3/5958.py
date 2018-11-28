#include <cstdio>
#include <cmath>
#include <memory.h>

bool checkFair(int i);

int main() 
{
    int t;
    scanf("%d", &t);
    int a, b;
    for (int caseNum = 1; caseNum <= t; ++caseNum)
    {
        scanf("%d %d", &a, &b);
        int count = 0;
        for (int i = a; i <= b; ++i)
        {
            double sqrtD = sqrt((double)i);
            int sqrtI = (int)sqrtD;
            if (sqrtI * sqrtI != i)
                continue;
            if (checkFair(i) && checkFair(sqrtI))
                ++count;
        }
        printf("Case #%d: %d\n", caseNum, count);
    }
    return 0;
}

bool checkFair(int i) 
{
    short tmp[101];
    int length = 0;
    while (i > 0)
    {
        tmp[length] = i % 10;
        i /= 10;
        ++length;
    }
    int head = 0, tail = length - 1;
    while (head < tail)
    {
        if (tmp[head] != tmp[tail])
            return false;
        ++head;
        --tail;
    }
    return true;
}
