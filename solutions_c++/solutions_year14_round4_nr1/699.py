#include <iostream>
#include <algorithm>
#include <set>
#include <cstdio>
using namespace std;
static inline void process(int t)
{
    int n, m;
    cin >> n >> m;
    multiset<int> s;
    for (int i = 0; i != n; i++)
    {
        int x;
        cin >> x;
        s.insert(x);
    }
    int ans = 0;
    while (!s.empty())
    {
        multiset<int>::iterator first = s.begin();
        int a = *first;
        s.erase(first);
        if (!s.empty())
        {
            multiset<int>::iterator it = s.upper_bound(m - a);
            if (it != s.begin())
            {
                s.erase(--it);
            }
        }
        ++ans;
    }
    printf("Case #%d: %d\n", t, ans);
}
int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
        process(i);
}
