#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <cstring>
#include <stack>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <climits>

#define ll long long
#define MAX(x,y) (((x)>(y))?(x):(y))
#define MIN(x,y) (((x)<(y))?(x):(y))
#define FOR(i,j,k) for(int i=j;i<=(k);i++)
#define REP(i,n)  for(int i=0;i<(n);i++)
#define mst(x,y) memset(x,y,sizeof(x))
#define eps 1e-5
#define INF 0x3f3f3f3f

using namespace std;

int T,smax;
char s[1005];

int main()
{
    scanf("%d",&T);
    for(int tt = 1;tt<=T;tt++)
    {
        scanf("%d",&smax);
        scanf("%s",s);
        int len = strlen(s);
        int cur = s[0]-'0';
        int ans = 0;
        for(int i=1;i<len;i++)
        {
            if(s[i]=='0') continue;
            if(cur >= i)
                cur += (s[i] - '0');
            else
            {
                ans += i-cur;
                cur = i + s[i] - '0';
            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
