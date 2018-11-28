#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;
const int MAX = 100000;
bool isPrime[MAX+9];
int total, n, j;
int prime[MAX+9], state[50], sprime[50];

void makePrime()
{
    memset(isPrime,true,sizeof(isPrime));
    memset(prime,0,sizeof(prime));
    for(int i=2; i<=MAX; i++)
    {
        if(isPrime[i]) prime[total++]=i;
        for(int j=0; j<total && (long long)i*prime[j]<=MAX; j++)
        {
            isPrime[i*prime[j]]=false;
            if(i%prime[j]==0) break;
        }
    }
}
long long change(long long x)
{
    long long tmp = 0;
    for (int i = n; i >= 1; --i)
    {
        tmp = tmp * x + state[i];
    }
    return tmp;
}
bool checkp(long long x, int ti)
{
    for (int i = 0; i <= 1000; ++i)
    {
        if (x % prime[i] == 0 && prime[i] < x)
        {
            sprime[ti] = prime[i];
            return false;
        }
    }
    return true;
}
bool check()
{
    long long bas[12];
    for (int i = 2; i <= 10; ++i)
    {
        bas[i] = change(i);
        if (checkp(bas[i], i)) return false;
    }
    for (int i = n; i >= 1; --i)
    {
        printf("%d", state[i]);
    }
    for (int i = 2; i <= 10; ++i)
    {
        printf(" %d", sprime[i]);
    }
    printf("\n");
    return true;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    makePrime();
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d:\n", cas);
        scanf("%d%d", &n, &j);
        state[n] = 1;
        state[1] = 1;
        for (int i = 0; i < 1 << (n - 2) && j; ++i)
        {
            int t = i;
            for (int k = 2; k <= n - 1; ++k)
            {
                state[k] = t % 2;
                t /= 2;
            }
            if (check()) j--;
        }
    }
    return 0;
}
