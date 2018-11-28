#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <utility>
#include <ctime>
#include <cassert>

#define F first
#define S second
#define pb push_back
#define mp make_pair
#define next stupid_next
#define prev stupid_prev

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int maxn = (int)5e3 + 10;
const int inf = (int)1e9;
const int mod = (int)1e9 + 7;
const ll INF = (ll)1e18;
const double eps = (int)1e-9;
const int alphabet = 26;

int l = maxn / 2, r = maxn / 2, t;
int prev[alphabet][maxn], next[alphabet][maxn];
char s[maxn], ans[maxn];

int main()
{
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
    {
        scanf("%s", s);
        l = r = maxn / 2;
        int n = strlen(s);
        ans[l] = s[0];
        for (int j = 1; j < n; ++j)
        {
            int pos = r + 1;
            for (int k = l; k <= r; ++k)
                if (s[j] != ans[k])
                {
                    pos = k;
                    break;
                }
            if (s[j] > ans[pos])
                ans[--l] = s[j];
            else
                ans[++r] = s[j];
        }
        printf("Case #%d: ", i + 1);
        for (int j = l; j <= r; ++j)
            printf("%c", ans[j]);
        puts("");
    }
    return 0;
}