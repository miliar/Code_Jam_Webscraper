#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <bitset>
#include <map>
#include <algorithm>
using namespace std;

typedef long long ll;

int K, C, S;

void domain()
{
    scanf("%d%d%d", &K, &C, &S);
    
    if (C == 1)
    {
        for (int i = 1; i <= K; ++i)    printf(" %d", i);
    }
    else
    {
        for (int i = 1; i <= K * K; i += K)    printf(" %d", i);
    }
    
    printf("\n");
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++ kase)
    {
        printf("Case #%d:", kase);
        
        domain();
    }
    
    return	0;
}
