#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

multiset <int, greater<int> > s;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        s.clear();
        int ans = 0;
        int n, x;
        scanf("%d %d", &n, &x);
        for (int i = 0; i < n; i++)
        {
            int elem;
            scanf("%d", &elem);
            s.insert(elem);
        }
        while(!s.empty())
        {
            ans++;
            set <int, greater<int> >::iterator e1 = s.begin();
            int ve1 = *e1;
            s.erase(e1);
            set <int, greater<int> >::iterator e2 = s.lower_bound(x - ve1);
            if (e2 != s.end())
                s.erase(e2);
        }
        printf("Case #%d: %d\n", i + 1, ans);
    }

    return 0;
}
