#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 1000000005
#define eps 1e-9
#define PI acos(-1.0)
#define K (0.017453292519943295769236907684886l)
#define LL long long

using namespace std;

const int maxn=1005;

char s[maxn];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        scanf("%s",s);
        int cur=0,ans=0;
        cur=s[0]-'0';
        for (int i=1;i<=n;i++)
        {
            if (cur<i)
            {
                ans=ans+i-cur;
                cur=i;
            }
            cur+=s[i]-'0';
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
