#include <bits/stdc++.h>
using namespace std;
#define MAX 10000009
#define ll long long

struct node
{
    ll num;
    ll div[15];
};

ll convert(ll x, int base);
int sieve();
void build();
int check(ll x);
int cnt_num(ll x);
ll convert(ll x, int base);
ll numPF(long long N);   // Count the number of prime factors of N
int gn(int left, int len, int i);

node arr[20][600];
int indx[300];
bool v[MAX];
int primes[MAX], p, k = 0;
ll arr2[(1 << 22) + 10], accum[30];
int m = 16;

int main()
{
    build();

    //freopen("C-small-attempt0", "r", stdin);
    freopen("c.out", "w", stdout);

    int tc, cases = 1;
    scanf("%d", &tc);

    while(tc--)
    {
        int length, j;
        scanf("%d %d", &length, &j);

        printf("Case #%d:\n", cases++);

        for(int i = 0; i < j; i++)
        {
            printf("%lld", arr[length][i].num);
            for(int k = 2; k <= 10; k++)
                printf(" %lld", arr[length][i].div[k]);

            printf("\n");
        }

    }
    return 0;

    for(int i = 0; i <= m; i++)
        printf("%d\n", indx[i]);

    return 0;
}

void build()
{
    p = sieve();
    memset(indx, 0, sizeof(indx));

    for(int i = 1; i <= m; i++)
        gn(i, i, 0);

    for(ll i = 0; i < k; i++)
        if(check(arr2[i]))
        {
            int flag = 0;

            for(int j = 2; j <= 10; j++)
                if(numPF(convert(arr2[i], j)) == -1)
                {
                    flag++;
                    break;
                }

            // printf("%lld\n", arr2[i]);

            if(flag == 0)
            {
                int l = cnt_num(arr2[i]);
                int in = indx[l];


                arr[l][in].num = arr2[i];

                for(int j = 2; j <= 10; j++)
                    arr[l][in].div[j] = numPF(convert(arr2[i], j));//
                if(indx[l] < 52)
                    indx[l]++;
            }
        }
}

int gn(int left, int len, int i)
{
    if(left == 0)
    {
        ll ret = 0;
        for(int i = 0; i < len; i++)
            ret = ret * 10 + accum[i];
        arr2[k++] = ret;

        return 0;
    }

    accum[i] = 1;
    gn(left - 1, len, i + 1);

    if(i != 0)
    {
        accum[i] = 0;
        gn(left - 1, len, i + 1);
    }

}

int check(ll x)
{
    if(x % 10 != 1)
        return 0;

    int prev = x % 10;

    while(x)
    {
        if(x % 10 != 0 && x % 10 != 1)
            return 0;

        prev = x % 10;
        x = x / 10;
    }

    return prev == 1;
}

int cnt_num(ll x)
{
    if(x == 0)return 1;
    int ret = 0;

    while(x)
        ret++, x = x / 10;

    return ret;
}

ll convert(ll x, int base)
{
    ll ret = 0;
    ll exp = 1;

    while(x)
    {
        ret += (x % 10) * exp;
        exp *= base;
        x = x / 10;
    }

    return ret;
}

int sieve()
{
    memset(v, 0, sizeof(v));
    v[0] = v[1] = 1;
    long long i, j;

    // Sieve of Eratosthenes
    for (i = 2; i * i < 10000001; i++)
    {
        if (!v[i])
        {
            for (j = i * i; j < 10000001; j += i)
            {
                v[j] = 1;
            }
        }
    }

    int index = 0;
    for (i = 2; i < 10000001; i++)
    {
        if (!v[i])
        {
            primes[index++] = i;
        }
    }

    return index;
}

ll numPF(long long N)   // Count the number of prime factors of N
{
    if(N == 1)
        return 2;
    int indx = 0;
    ll counter = 0;
    ll ret = 0;
    int index = 0;
    ll tmp;
    long long pf = primes[index++];
    int fact = 0;

    while (N != 1 && index < p && N > pf * pf) // && pf * pf <= N)
    {
        tmp = 1;
        counter = 0;
        while (N % pf == 0)
        {
            return pf;
            N /= pf;
            tmp *= pf;
            counter++;
        }

        if(counter)
            ret += tmp, fact++;

        pf = primes[index++];
    }

    if (N != 1)
        ret += N, fact++;

    if (fact == 1)
        ret++;

    return -1;
}
