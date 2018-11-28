#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int a[2000];
int b[2000];

bool check_ud(int n, vector<int> &v)
{
    for (int i = 0; i < n; ++i)
    {
        bool f = true;
        for (int j = 0; j < i; j++)
            if (a[j] > a[j + 1])
            {
                f = false;
                break;
            }
        for (int j = i; j < n; ++j)
            if (a[j] < a[j + 1])
            {
                f = false;
                break;
            }
        if (f)
            return true;

    }
    return false;
}

int cnt_inv(int n, vector<int> &v)
{
    int ans = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (a[i] == v[j])
                ans += abs(i - j);
    return ans / 2;
}

int stupid_solution(int n)
{
    vector<int> v(n);
    for (int i = 0; i < n; ++i)
        v[i] = a[i];
    sort(v.begin(), v.end());
    int ans = 1000000000;
    do
    {
        if (check_ud(n, v))
            ans = min(ans, cnt_inv(n, v));
    } while (next_permutation(v.begin(), v.end()));
    return ans;
}

int solution(int n)
{
    set<pair<int, int> > s;
    for (int i = 0; i < n; ++i)
    {
        s.insert(make_pair(a[i], i));
        b[i] = 1;
    }
    int ans = 0;
    while (!s.empty())
    {
        int k = s.begin()->second;
        s.erase(s.begin());
        b[k] = 0;
        int rv = 0, lv = 0;
        for (int i = 0; i < k; ++i)
            lv += b[i];
        for (int i = k; i < n; ++i)
            rv += b[i];
        ans += min(lv, rv);
    }
    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int q = 0; q < t; ++q)
    {
        printf("Case #%d: ", q + 1);
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%d", &a[i]);
        printf("%d\n", solution(n));
    }
    return 0;

}
