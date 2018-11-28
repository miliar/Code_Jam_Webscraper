#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
using namespace std;

int smax;
string s;
int a[100000];

int solve()
{
    int tot = 0;
    for(int i = 0; i <= smax; i++)
    {
        for(int j = 0; j < int(s[i] - '0'); j++) a[tot++] = i;
    }
    sort(a, a + tot);
    int stand = 0, res = 0;
    for(int i = 0; i < tot; i++)
    {
        if(a[i] > stand)
        {
            res += (a[i] - stand);
            stand += (a[i] - stand);
        }
        stand++;
    }
    return res;
}

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);
    int testcnt;
    cin >> testcnt;
    for(int i = 1; i <= testcnt; i++)
    {
        cin >> smax >> s;
        printf("Case #%d: %d\n", i, solve());
    }
}
