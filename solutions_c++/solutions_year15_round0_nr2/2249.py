#include <iostream>
#include <cstdio>

using namespace std;

const int N = 1005;
int mem[N][N];
int reduce_time(int x, int k)
{
    if(x <= k) return 0;
    if(mem[x][k] > 0) return mem[x][k];
    mem[x][k] = 1 << 30;
    for(int i = 1; i < x; i++)
        mem[x][k] = min(mem[x][k], (reduce_time(i, k) + reduce_time(x - i, k)) + 1);
    return mem[x][k];
}

int plate[N];

int main()
{
    freopen("b-large.in", "r", stdin);
    freopen("large.out", "w", stdout);

    int test;
    scanf("%i", &test);

    for(int t = 1; t <= test; t++)
    {
        fprintf(stderr, ".");
        int n;
        scanf("%i", &n);
        for(int i = 0; i < n; i++) scanf("%i", &plate[i]);

        int res = 1 << 30;
        for(int k = 1; k < N; k++)
        {
            int cnt = 0;
            for(int i = 0; i < n; i++) cnt += reduce_time(plate[i], k);
            res = min(res, cnt + k);
        }

        printf("Case #%i: %i\n", t, res);
    }
    return 0;
}
