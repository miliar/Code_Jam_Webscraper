#include <stdio.h>
#include <math.h>

int N, J;
__int64 baseNumArr[11];
__int64 jamCoinArr[11];

void SetBaseNumber()
{
    for (__int64 i = 2; i <= 10; ++i)
    {
        baseNumArr[i] = i;

        for (__int64 j = 0; j < N - 2; ++j)
        {
            baseNumArr[i] *= i;
        }

        baseNumArr[i] += 1;
        //baseNumArr[i] = (unsigned long long)powl(i, N - 1) + 1;
    }
}

bool JamCheck()
{
    bool result = true;
    __int64 t = baseNumArr[2];
    __int64 idx = 0;

    for (__int64 i = 3; i <= 10; ++i)
        baseNumArr[i] = 0;

    while (t)
    {
        if (t % 2 == 1)
        {
            __int64 powering;

            for (__int64 i = 3; i <= 10; ++i)
            {
                powering = 1;
                for (__int64 j = 0; j < idx; ++j)
                {
                    powering *= i;
                }
                baseNumArr[i] += powering;
            }
        }

        ++idx;
        t /= 2;
    }

    __int64 len = 0;
    __int64 testN;

    for (__int64 i = 2; i <= 10; ++i)
    {
        len = sqrtl(baseNumArr[i]) + 1;
        for (testN = 2; testN < len; ++testN)
        {
            if (baseNumArr[i] % testN == 0)
            {
                jamCoinArr[i] = baseNumArr[i] / testN;
                //jamCoinArr[i] = testN;
                break;
            }
        }

        if (testN == len)
        {
            result = false;
            break;
        }
    }

    return result;
}

void PrintJamCoin()
{
    // print binary
    int t = baseNumArr[2];
    int idx = 0;
    char str[32];

    while (t)
    {
        str[idx++] = t % 2 == 1 ? '1' : '0';
        t /= 2;
    }

    for (int i = N - 1; i >= 0; --i)
        putchar(str[i]);

    for (int i = 2; i <= 10; ++i)
    {
        //printf(" %lld", baseNumArr[i]);
        printf(" %lld", jamCoinArr[i]);
    }

    putchar('\n');
}

void Find()
{
    int i = 0;
    while (J)
    {
        if (JamCheck())
        {
            PrintJamCoin();
            --J;
        }

        for (i = 2; i <= 10; ++i)
        {
            baseNumArr[i] += i;
        }
    }
}

int main()
{
    int testN;
    scanf_s("%d", &testN);

    scanf_s("%d%d", &N, &J);

    printf("Case #1:\n");
    SetBaseNumber();
    Find();
}