#include <bits/stdc++.h>

using namespace std;

int test , T , n , i;
set < int > mset;

void cnt(long long x)
{
    while (x)
    {
        mset.insert(x % 10);
        x /= 10;
    }
}

int main()
{
freopen("test.in" , "r" , stdin);
freopen("test.out" , "w" , stdout);

scanf("%d" , &T);
for (test = 1 ; test <= T ; ++test)
{
    scanf("%d" , &n);
    mset.clear();

    for (i = 1 ; i <= 100000 ; ++i)
    {
        cnt(1LL * n * i);
        if (mset.size() == 10) break;
    }

    printf("Case #%d: " , test);
    if (i == 100001) printf("INSOMNIA\n");
    else printf("%lld\n" , 1LL * i * n);
}

return 0;
}
