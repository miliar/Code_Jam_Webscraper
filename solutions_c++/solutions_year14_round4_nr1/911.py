#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int MaxN = 10000;

int N, X;
int A[MaxN];
int f[MaxN][MaxN];

int solve(int p, int q)
{
    if(f[p][q] >= 0)
        return f[p][q];
    if(p == 0 && q == N)
        return 0;
    
    int val = 0x6fffffff;
    
    if(p > 0) val = min(val, solve(p-1, q) + 1);
    if(q < N) val = min(val, solve(p, q+1) + 1);
    if(p > 0 && q < N && A[p-1] + A[q] <= X)
        val = min(val, solve(p-1, q+1) + 1);
    
    f[p][q] = val;
    
    //printf("f[%d][%d] = %d\n", p, q, val);
    return val;
}


int main()
{
    int T;
    
    cin >> T;
    
    for(int c=0; c<T; c++)
    {
        cin >> N >> X;
        for(int i=0; i<N; i++)
            cin >> A[i];
        
        sort(A, A+N);
        
        memset(f, -1, sizeof(f));
        
        int r = 0x6fffffff;
        for(int i=0; i<N; i++)
        {
            int val = solve(i, i);
            r = min(r, val);
        }
        
        int result = r;
        
        printf("Case #%d: %d\n", c+1, result);
    }
    
    return 0;
}

