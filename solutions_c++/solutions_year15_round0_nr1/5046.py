#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <vector>
using namespace std;
#define pb push_back
#define For(i, n) for(int i = 0; i < (n); i++)
#define ForD(i, n) for(int i = (n) - 1; i >= 0; i--)
typedef long long LL;

int main()
{
    int t;
    scanf("%d", &t);
    
    For (k, t)
    {
        int n;
        scanf("%d", &n);
        
        const int N = 1001;
        int A[N] = {};
        
        For (i, n + 1)
            scanf(" %c", &A[i]),
            A[i] -= '0';
        
        int cnt = 0;
        int res = 0;
        
        For (i, n + 1)
            res += i > cnt + res ? i - cnt - res : 0,
            cnt += A[i];
        
        printf("Case #%d: %d\n", k + 1, res);
    }
}