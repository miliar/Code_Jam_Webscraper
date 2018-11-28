// CodeJam2016-2.cpp : Defines the entry point for the console application.
//


#include <fstream>
#include <sstream>
#include <string>
#include <bitset>

uint64_t pow(int base, int exp)
{
    uint64_t num = 1;
    for (int i = 0; i < exp; i++)
    {
        num *= base;
    }
    return num;
}

void tile(int K, int C, int S)
{
    if (K == 1)
    {
        printf("1");
        return;
    }
    else if (K == 2)
    {
        printf("1 %lld", pow(K, C));
        return;
    }

    uint64_t diff = pow(K, C) / (K - 1);
    for (int i = 0; i < K; i++)
    {
        printf("%lld ", 1 + i * diff);
    }
}

int main()
{
    std::ifstream input("4.in");

    int cases = 0;
    input >> cases;

    for (int caseNumber = 0; caseNumber < cases; caseNumber++)
    {
        int K, C, S;
        input >> K >> C >> S;

        printf("Case #%d: ", caseNumber + 1);

        if (S < K)
        {
            printf("IMPOSSIBLE");
        }
        else
        {
            tile(K, C, S);
        }

        printf("\n");
    }

    getchar();

    return 0;
}

