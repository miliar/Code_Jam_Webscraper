#include <functional>
#include <algorithm>
#include <iostream>

using namespace std;

int a[1009], b[1009];
int pw(int x, int y)
{
    int ans = 1;
    for (int i = 1; i <= y; ++i)
    {
        ans *= x;
    }
    return ans;
}
int val(int data, int tot, int pos)
{
    return data * a[tot] *  pw(-1, pos);
}
struct P
{
    int left, right, data;
} p[1009];
int main()
{
    freopen("in.txt","r",stdin);
    int t;
    scanf("%d",&t);
    int n;
    for (int cas = 1; cas <= t; ++cas)
    {
        printf("Case #%d: ", cas);
        scanf("%d",&n);
        for (int i = 1; i <= n; ++i)
        {
            scanf("%d", &a[i]);
            b[i] = a[i];
        }
        sort(b + 1, b + 1 + n);
        int root = n;
        p[root].data = a[n];
        int left = n, right = n;
        for (int i = n - 1; i >= 1; --i)
        {
            if (val(a[i], n - i, 0) < val(a[i], n - i, 1))
            {
                p[left].left = i;
                left = i;
                p[left].data = a[i];
            }
            else
            {
                p[right].right = i;
                right = i;
                p[right].data = a[i];
            }
        }
    }
            return 0;
}
