#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

bool f[10];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int ti = 1; ti <= t; ti++)
    {
        memset(f, false, sizeof(f));
        long long n;
        cin >> n;
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", ti);
            continue;
        }
        long long sum = 0;
        int tmp = 0;
        while(tmp < 10)
        {
            sum++;
            long long item = sum * n;
            while(item > 0)
            {
                int p = item % 10;
                if(!f[p])
                {
                    f[p] = true;
                    tmp++;
                }
                item = item / 10;
            }
        }
        printf("Case #%d: %d\n", ti, sum * n);
    }
    return 0;
}
