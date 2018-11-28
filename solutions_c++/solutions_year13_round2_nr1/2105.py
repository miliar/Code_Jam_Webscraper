#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define foreach(i, c) for (__typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)

int A;
int a[110];
int n;

int ans;

void check(int mask)
{
    vector<int> b;
    for (int i = 0 ;i<n;i++)
    {
        if (mask & (1<<i))
        {
            b.push_back(a[i]);
        }
    }

    int count = n - b.size();    
    int csize = A;
    foreach(iter, b)
    {
        if (*iter < csize)
        {
            csize += *iter;
        }
        else
        {
            if (csize == 1)
                return;

            int k = 0;
            while (*iter >= csize)
            {
                csize += csize - 1;
                k ++;
            }
            count += k;
            csize += *iter;
        }
    }

    if (count < ans)
        ans = count;
}

void work()
{
    memset(a, 0, sizeof(a));
    scanf("%d%d", &A, &n);
    for (int i = 0;i<n;i++)
        scanf("%d", &a[i]);
    sort(a, a + n);

    ans = n;

    for (int mask = 0; mask < (1<<n); mask++)
    {
        check(mask);
    }
    printf("%d\n", ans);
}
 
int main()
{
    // freopen("A-small-practice.in", "r", stdin);
    // freopen("A-large-practice.in", "r", stdin);    
    freopen("a0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
 
    int t;
    scanf("%d", &t);
    for (int cs = 1; cs <= t; cs++)
    {
        printf("Case #%d: ", cs);
        work();
    }
 
    return 0;
}