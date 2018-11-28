#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

const int MAXN = 1000 + 10;

double A[MAXN], B[MAXN];
int n;

void init()
{
    scanf("%d", &n);
    for (int i=0; i<n; i++)
        scanf("%lf", &A[i]);
    for (int i=0; i<n; i++)
        scanf("%lf", &B[i]);
    sort(A, A+n);
    sort(B, B+n);
}

int work1()
{
    int res = n;
    int l = 0, r = n-1;
    int r2 = n-1;
    while (l <= r)
    {
        if (B[r2] >= A[r])
        {
            res --;
            l ++;
            r2 --;
        }
        else
        {
            r --;
            r2 --;
        }
    }
    return res;
}

int work2()
{
    int res = n;
    int l = 0;
    for (int i=0; i<n; i++)
    {
        if (B[i] > A[l])
        {
            res --;
            l ++;
        }
    }
    return res;
}


int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int tim=1; tim<=T; tim++)
    {
        init();
        printf("Case #%d: %d %d\n", tim, work1(), work2());
    }
    
}
