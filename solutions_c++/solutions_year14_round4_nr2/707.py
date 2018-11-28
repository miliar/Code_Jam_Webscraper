#include <iostream>
#include <map>
#include <algorithm>
#include <climits>
using namespace std;
int a[1001];
int b[1001];
map<int ,int> pos;
int n;
static int my_abs(int x)
{
    if (x < 0)
        return -x;
    return x;
}
static void process(int t)
{
    int ans = 0;
    pos.clear();
    cin >> n;
    for (int i = 0; i < n ; ++i)
    {
        cin >> a[i];
        b[i] = a[i];
        pos[a[i]] = i;
    }
    sort(b, b + n);
    int used = 0;
    int left = 0;
    int right = n - 1;
    while (used < n)
    {
        int cost1 = pos[b[used]] - left;
        int cost2 = right - pos[b[used]];
        if (cost1 < cost2)
        {
            ans += cost1;
            for (int i = 0 ; ; ++i)
                if (a[i] == b[used])
                    break;
                else
                    ++pos[a[i]];
            ++left;
        }
        else
        {
            ans += cost2;
            for (int i = n - 1 ; ; --i)
                if (a[i] == b[used])
                    break;
                else
                    --pos[a[i]];
            --right;
        }
        ++used;
    }
    printf("Case #%d: %d\n", t, ans);
}
int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
        process(i);
    return 0;
}
