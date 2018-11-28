#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>
#include <set>

using namespace std;

struct comp
{
    bool operator()(int a, int b)
    {
        return a > b;
    }
};

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int z =1; z <= t; ++z)
    {
        printf("Case #%d: ", z);
        int n, x;
        scanf("%d %d", &n, &x);
        multiset <int, comp> s;
        for (int i = 0; i < n; ++i)
        {
            int a;
            scanf("%d", &a);
            s.insert(a);
        }
        int answer = 0;
        while (s.size())
        {
            int cur = *s.begin();
            s.erase(s.begin());
            auto y = s.lower_bound(x - cur);
            if (y != s.end())
            {
                s.erase(y);
            }
            ++answer;
        }
        printf("%d\n", answer);
    }
    return 0;
}