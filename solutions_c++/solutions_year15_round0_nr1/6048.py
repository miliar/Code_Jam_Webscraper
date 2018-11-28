#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <sstream>
#include <fstream>
#define debug puts("-----")
#define ll long long int
const double pi = acos(-1.0);
const double eps = (1e-8);
const int inf = 1 << 31;
using namespace std;

const int MAXN = 10000 + 5;

char s[MAXN];
int t, n;
int cas = 0;
int ans, sum;

void init()
{
    ans = 0, sum = 0;
    scanf("%d", &n);
    scanf("%s", s);

}

int main(int argc, char const *argv[])
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%d", &t);
    while (t--)
    {
        init();
        for (int i = 0; i <= n; i++)
        {
            if (i - sum > 0) ans += i - sum, sum += i - sum;
            sum += s[i] - '0';
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}

