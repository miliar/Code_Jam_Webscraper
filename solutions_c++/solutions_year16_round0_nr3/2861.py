// RandomUsername (Nikola Jovanovic)
// GCJ 2016 Q
// B

#include <bits/stdc++.h>
#define DBG false
#define debug(x) if(DBG) printf("(ln %d) %s = %d\n", __LINE__, #x, x);
#define lld long long
#define ff(i,a,b) for(int i=a; i<=b; i++)
#define fb(i,a,b) for(int i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2
#define INF 2000000000
#define MAXT 105
#define MAXLEN 10000005
#define EPS 1e-6
#define MAXN 10000005
#define MAXL 50

using namespace std;

lld n, j;
int s[MAXL];
lld N;

lld comp[MAXN];

void sieve(lld n)
{
    for(lld i = 1; i <= n; i++)
        comp[i] = -1;
    comp[1] = 1;
    for(lld i = 2; i <= n; i++)
    {
        if(-1 == comp[i])
        {
            for(lld j = i*i; j <= n; j += i)
            {
                comp[j] = i;
            }
        }
    }
}

lld getNum(lld base)
{
    lld ret = 0;
    lld curr = 1;
    fb(i, 15, 0)
    {
        ret += s[i] * curr;
        curr *= base;
    }
    return ret;
}

lld proofs[15];

lld findFactor(lld num)
{
    lld limit = sqrt(num);
    ff(i, 2, limit)
    {
        if(num%i == 0)
        {
            return i;
            // prime factor!
        }
    }
    return -1;
}

void test()
{
    bool good = true;

    if(j == 0) return;
    // we need more
    for(lld i = 2; i <= 10; i++)
    {
        lld num = getNum(i);
        lld tmp;
        if(num <= N)
        {
            tmp = comp[num];
        }
        else tmp = findFactor(num);

        if(tmp == -1)
        {
            good = false;
            break;
        }
        else
        {
            proofs[i] = tmp;
        }
    }
    if(good)
    {
        ff(i, 0, 15)
            printf("%d", s[i]);
        ff(i, 2, 10)
            printf(" %d", proofs[i]);
        printf("\n");
        j--;
    }
    return;
}

void genAll(int idx)
{
    if(idx == 15)
    {
        test();
        return;
    }
    s[idx] = 0;
    genAll(idx+1);
    s[idx] = 1;
    genAll(idx+1);
}

int main()
{
    freopen("c.out", "w", stdout);
    n = 16;
    j = 50;
    N = 10000000;
    sieve(N);
    printf("Case #1:\n");
    s[0] = s[15] = 1;
    genAll(1);
    return 0;
}
