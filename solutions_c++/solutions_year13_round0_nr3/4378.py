#include <cstdio>
#include <string.h>
#include <cmath>
#include <vector>
using namespace std;

long long maxn = 100000000000000LL;

vector <long long> fs;

bool parli(char str[], int lf, int rt)
{
    while ( lf < rt && str[lf] == str[rt] )
        lf ++, rt --;
    if (lf < rt)
        return false;
    return true;
}

int bisearch_lf(long long key)
{
    int lf = 0, rt = fs.size() - 1;
    while (lf <= rt)
    {
        int mid = (lf + rt) >> 1;
        if (fs[mid] >= key )
            rt = mid - 1;
        else lf = mid + 1;
    }
    if (rt >= 0 && fs[rt] >= key)
        return rt;
    if (lf < fs.size() && fs[lf] >= key)
        return lf;
    return -1;
}

int bisearch_rt(long long key)
{
    int lf = 0, rt = fs.size() - 1;
    while (lf <= rt)
    {
        int mid = (lf + rt) >> 1;
        if (fs[mid] > key )
            rt = mid - 1;
        else lf = mid + 1;
    }

    if (lf < fs.size() && fs[lf] <= key)
        return lf;
    if (rt >= 0 && fs[rt] <= key)
        return rt;
    return -1;
}

int main()
{
    fs.clear();
    char str[200];
    for (long long i = 1LL;  ;i ++)
    {
        if ( i*i > maxn )
            break;
        sprintf(str, "%lld", i);
        if (parli(str, 0, strlen(str) - 1))
        {
            sprintf(str, "%lld", i*i);
            if (parli(str, 0, strlen(str) - 1))
            {
                fs.push_back(i*i);
                //printf("%d ", i*i);
            }
        }
    }
    //printf("size = %d\n", fs.size());
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);
    int t, cas = 1;
    scanf("%d", &t);
    //printf("%d\n", t);
    while (t --)
    {
        long long a, b;
        scanf("%lld %lld", &a, &b);
        int lf = bisearch_lf(a);
        int rt = bisearch_rt(b);
        int ans = 0;
       // printf("%d, %d\n", lf, rt);
        if (lf != -1 && rt != -1 && rt >= lf)
            ans = rt - lf + 1;
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
