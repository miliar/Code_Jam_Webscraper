//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <functional>
using namespace std;
const int N = 1003, W = 1003;

int n;
int A[N];

bool check(int r, int x)
{
    if(x-r <= 0) return false;

    int uzyte = 0;
    for(int i = 1;i <= n;i++)
    {
        uzyte += (A[i]-1)/(x-r);
        if(uzyte > r) return false;
    }
    return true;
}

int bin(int r, int p, int k)
{
    int sr;
    while(p < k)
    {
        sr = (p+k)/2;
        if(check(r, sr)) k = sr;
        else p = sr+1;
    }
    return k;
}

int main()
{
    int t;
    scanf("%d", &t);
    for(int ti = 1;ti <= t;ti++)
    {
        scanf("%d", &n);
        for(int i = 1;i <= n;i++)
            scanf("%d", &A[i]);
        
        sort(A+1,A+n+1, greater<int>());
        
        int wyn = W;
        for(int r = 0;r <= W;r++)
        {
            int twyn = bin(r, 1, W+1);
            wyn = min(wyn, twyn);
        }

        printf("Case #%d: %d\n", ti, wyn);
    }
    return 0;
}
