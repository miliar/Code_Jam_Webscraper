#include <bits/stdc++.h>

using namespace std;
int t, T, d, x;
int solve(multiset<int, greater<int> >s)
{
    x = *s.begin();
    if(x <= 3)
        return x;
    multiset<int, greater<int> >ss;
    for(auto it : s)
        ss.insert(it - 1);
    s.erase(s.begin());
    if(x==9)
    {
        s.insert(3);
        s.insert(6);
    }
    else
    {
         s.insert(x / 2);
        s.insert(x - (x / 2));
    }
    return min(solve(s), solve(ss)) + 1;
}
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &t);
    for(T = 1; T <= t; T++)
    {
        scanf("%d", &d);
        multiset<int, greater<int> >s;
        for(; d; d--)
        {
            scanf("%d", &x);
            s.insert(x);
        }
        printf("Case #%d: %d\n", T, solve(s));
    }
    return 0;
}
