#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int res, maxP;
vector<int> cakes;
map<string, int> memo;

string mapit(vector<int> cur)
{
    sort(cur.begin(), cur.end());
    string mapped = "";
    for (vector<int>::iterator it = cur.begin(); it != cur.end(); it++)
        mapped += (char)(*it + '0');
    return mapped;
}

int doit(vector<int> cur)
{
    if (cur.size() == 0)
    {
        return 0;
    }

    int res = maxP;
    string mappedString = mapit(cur);
    if (memo.find(mappedString) != memo.end())
        return memo[mappedString];

    vector<int> now1;
    for (vector<int>::iterator it = cur.begin(); it != cur.end(); it++) if (*it > 1) now1.push_back(*it - 1);
    res = min(res, 1 + doit(now1));

    for (int i = 0; i < cur.size(); i++)
    {
        int nn = cur[i];
        if (nn > 1)
        {
            for (int j = 1; j <= nn / 2; j++)
            {
                vector<int> now2 = cur;
                now2[i] = j;
                now2.push_back(nn - j);
                res = min(res, 1 + doit(now2));
            }
        }
    }

    memo[mappedString] = res;
    return res;
}

void _main()
{
    int D, P;
    scanf("%d", &D);
    cakes.clear();
    for (int i = 0; i < D; i++)
    {
        scanf("%d", &P);
        cakes.push_back(P);
        maxP = max(P, maxP);
    }

    printf("%d\n", doit(cakes));
}

int main()
{
    freopen("B-small-attempt6.in", "r", stdin);
    freopen("B-small.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++)
    {
        printf("Case #%d: ", cases);
        _main();
    }
}