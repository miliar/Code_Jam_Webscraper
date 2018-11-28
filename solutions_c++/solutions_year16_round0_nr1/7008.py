#include <bits/stdc++.h>

using namespace std;

int a[15];
long long n;

int check()
{
    int i;
    for(i=0; i<10; i++)
    {
        if(a[i]==0) return 0;
    }
    return 1;
}

long long call(long long x)
{
    long long cd = x;
    while(x!=0)
    {
        int m = x%10;
        x = x/10;
        a[m] = 1;
    }
    if(check()) return cd;
    else call(cd+n);
}



int main()
{
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    int tc, i;
    scanf("%d", &tc);
    for(i=1; i<=tc; i++)
    {
        memset(a, 0, sizeof(a));
        scanf("%lld", &n);
        if(n==0) printf("Case #%d: INSOMNIA\n", i);
        else
        {
            printf("Case #%d: %lld\n", i, call(n));
        }
    }
    return 0;
}


