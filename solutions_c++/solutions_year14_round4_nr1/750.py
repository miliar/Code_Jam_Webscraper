
#include <string>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <functional>
#include <stack>
#include <set>
#include <queue>
#include <cmath>
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

typedef long long ll;
const double eps = 1e-6;
const int maxint = -1u>>2;

int n,x,s[11000];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    scanf("%d",&T);

    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d%d",&n, &x);
        for(int i=0;i<n;i++)
        {
            scanf("%d", &s[i]);
        }
        sort(s, s+n);
        int ans = 0;
        for(int i=n-1, j=0;i>=j;)
        {
            if(s[i] + s[j] <= x)
            {
                ans++;
                i--;
                j++;
            }
            else if(s[i] <= x)
            {
                ans++;
                i--;
            }
            else
            {
                printf("Error\n");
            }
        }
        printf("Case #%d: %d\n",cas,  ans);
    }

    return 0;
}

