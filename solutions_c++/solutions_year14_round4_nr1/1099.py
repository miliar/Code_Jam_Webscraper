#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 100005;
int a[N];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int test;
    scanf("%i", &test);

    for(int t = 0; t < test; t++)
    {
        int res = 0;
        int n, cap;
        scanf("%i %i", &n, &cap);
        for(int i = 0; i < n; i++) scanf("%i", &a[i]);

        sort(a, a + n);
        int j = n - 1;
        for(int i = 0; i < j; i++)
        {
            while(i < j && a[i] + a[j] > cap) j--;
            if(i < j) { res--; j--; }
        }
        res += n;

        printf("Case #%i: %i\n", t + 1, res);
    }
    return 0;
}
