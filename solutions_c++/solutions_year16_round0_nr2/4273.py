#include <cstdio>
#include <cstring>
#include <algorithm>
#include <climits>
#include <cctype>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const double pi = acos(-1.0);
const int inf = 0x7fffffff;
const int mod = 1e8 + 7;

char s[110];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out","w",stdout);
    int t,k = 1;
    scanf("%d",&t);
    while (t --)
    {
        scanf("%s",s);
        int len = strlen(s);
        int sum = 0;
        char cur = '+';
        for (int i = len - 1;i >= 0; -- i)
        {
            if (s[i] != cur)
            {
                ++ sum;
                cur = s[i];
            }
        }
        printf("Case #%d: %d\n",k ++,sum);
    }
    return 0;
}
