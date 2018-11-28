#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int n=16, j=50;
    printf("Case #1:\n");
    for (int k=0; k<j; k++)
    {
        printf("1");
        for (int i=0; i<7; i++)
            if (k & (1<<i))
                printf("11");
            else
                printf("00");
        printf("1 3 4 5 6 7 8 9 10 11\n");
    }
    return 0;
}
