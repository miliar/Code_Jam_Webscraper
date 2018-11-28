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

char S[1001], C;

void _main()
{
    scanf("%d%s", &C, S);

    int need = 0;
    int cur = S[0] - '0';
    for (int i = 1; i < C + 1; i++)
    {
        if (S[i] == '0') continue;

        if (i <= cur)
        {
            cur += S[i] - '0';
        }
        else
        {
            need += i - cur;
            cur += need + S[i] - '0';
        }
    }
    printf("%d\n", need);
}

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++)
    {
        printf("Case #%d: ", cases);
        _main();
    }
}