#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <queue>
#include <stack>
#include <map>
#include <cmath>

#pragma comment(linker, "/STACK:1024000000")
#define LL long long int
#define INF 0x3f3f3f3f

using namespace std;

char s[1010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n;

    int T,icase = 1;

    int sum,i,ans;

    scanf("%d",&T);

    while(T--)
    {
        scanf("%d %s",&n,s);

        for(ans = 0,sum = s[0]-'0',i = 1;s[i] != '\0'; ++i)
        {
            if(i > sum)
                ans += i-sum,sum += i-sum;
            sum += s[i]-'0';
        }

        printf("Case #%d: %d\n",icase++,ans);
    }

    return 0;
}
