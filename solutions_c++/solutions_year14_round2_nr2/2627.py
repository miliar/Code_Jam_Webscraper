#include <cassert>
#include <cstdio>
#include <iostream>
#include <map>

int A, B, K;

int answer()
{
    int minNum = std::min(A, B);
    int maxNum = std::max(A, B);
    int count = 0;

    for (int i = 0; i < minNum; i++)
    {
        for (int j = 0; j < maxNum; j++)
        {
            if ((i & j) < K)
            {
                count++;
            }
        }
    }

    return count;
}

int main()
{
    int testCases = 0;


    FILE* fp = fopen("test_in_small.txt", "r");
    fscanf(fp, "%d\n", &testCases);

    for (int i = 0; i < testCases; i++)
    {
        fscanf(fp, "%d %d %d\n", &A, &B, &K);
        printf("Case #%d: %d\n", i+1, answer());
    }

    return 0;
}