#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <bitset>
#include <map>
#include <algorithm>
using namespace std;

typedef long long ll;

char s[120];
int N;

void domain()
{
    N = (int)strlen(s);
    
    int A = 0;//prefix up
    int B = 0;//prefix down
    
    for (int i = 0; i < N; ++i)
    {
        if (s[i] == '+')
        {
            B = min(A + 1, B + 2);
        }
        else
        {
            A = min(B + 1, A + 2);
        }
    }
    
    printf("%d\n", A);
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++ kase)
    {
        printf("Case #%d: ", kase);
        scanf("%s", s);
        domain();
    }
    
    return	0;
}
