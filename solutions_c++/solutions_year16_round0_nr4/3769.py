#include <algorithm>
#include <string.h>
#include <vector>
#include <cstdio>
#include <climits>
#include <iostream>
using namespace std;
typedef unsigned long long lld;

void Process()
{
    int K, C, S;
    scanf("%d %d %d", &K, &C, &S);

    for (int i=1; i<=K; i++)
    {
        printf("%d", i);
        printf("%c", (i == K) ? '\n' : ' ');
    }
}


int main ()
{
    freopen("input.txt", "r", stdin);
    freopen("otp.txt", "w", stdout);

    int tests;
    scanf("%d", &tests);
    for (int t=1; t<=tests; t++)
    {
        printf("Case #%d: ", t);
        Process();
    }
}

