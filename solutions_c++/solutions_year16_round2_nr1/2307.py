#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int const maxN = 2010;

string d[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int cnt[40];
char s[maxN];
vector<int> res;

void check(char c, int num)
{
    int k = 1e9;
    for (int i = 0; i < d[num].size(); i++)
    {
        int p = 0;
        for (int j = 0; j < d[num].size(); j++)
        {
            p += d[num][j] == d[num][i];
        }
        k = min(k, cnt[d[num][i] - 'A'] / p);
    }
    for (int i = 0; i < k; i++)
        res.push_back(num);
    for (int i = 0; i < d[num].size(); i++)
    {
        cnt[d[num][i] - 'A'] -= k;
    }
}

void solve()
{
    res.clear();
    check('Z', 0);
    check('W', 2);
    check('U', 4);
    check('X', 6);
    check('G', 8);
    check('O', 1);
    check('T', 3);
    check('F', 5);
    check('S', 7);
    check('I', 9);
    sort(res.begin(), res.end());
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int q;
    scanf("%d\n", &q);
    for (int t = 1; t <= q; ++t)
    {
        memset(cnt, 0, sizeof(cnt));
        printf("Case #%d: ", t);
        scanf("%s", &s);
        int n = strlen(s);
        for (int i = 0; i < n; i++)
        {
            cnt[s[i] - 'A']++;
        }
        solve();
        for (int i = 0; i < res.size(); ++i)
        {
            printf("%d", res[i]);
        }
        printf("\n");
    }
    return 0;
}