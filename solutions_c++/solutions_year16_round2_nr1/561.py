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

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int maxn = (int)1e6 + 10;
const int inf = (int)1e9;
const int mod = (int)1e9 + 7;
const ll INF = (ll)1e18;
const double eps = (int)1e-9;

int a[10] =  {0,   2,    4,   6,   8,   1,   3,   5,   7,   9};
char c[10] = {'Z', 'W', 'U', 'X', 'G', 'O', 'H', 'F', 'S', 'E'};
string str[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR",
                 "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};


char res[2000];
char s[2010];

int ans[10], cnt[300];

char *solve()
{
    scanf("%s", s);
    int n = strlen(s);
    int sz = 0;
    
    for (int i = 0; i < 300; ++i)
        cnt[i] = 0;
    for (int j = 0; j < n; ++j)
        cnt[s[j]]++;
    
    for (int i = 0; i < 10; ++i)
    {
        ans[a[i]] = cnt[c[i]];
        int t = str[a[i]].length();
        for (int j = 0; j < t; ++j)
            cnt[str[a[i]][j]] -= ans[a[i]];
    }
    
    for (int i = 0; i < 10; ++i)
        for (int j = 0; j < ans[i]; ++j)
            res[sz++] = i + '0';
    
    res[sz] = 0;
    
    return res;
}

int main()
{
    int test;
    scanf("%d", &test);
    for (int i = 0; i < test; ++i)
        printf("Case #%d: %s\n", i + 1, solve());
    return 0;
}