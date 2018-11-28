#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#define MAXN 1000000

using namespace std;

char s[2001];

int main()
{
    int t,i,r,n,x;
    int stand;
    int sum;
    freopen("A-large.in","r",stdin);
    freopen("A-large-output0.txt","w",stdout);
    scanf("%d",&t);
    for(r=1;r<=t;r++)
    {
        scanf("%d %s",&n,s);
        stand=0;
        sum=0;
        for(i=0;i<=n;i++)
        {
            x=s[i]-'0';
            sum+=x;
            if(stand<i&&x>0)
            {
                stand=i;
            }
            stand+=x;
        }
        printf("Case #%d: %d\n",r,stand-sum);
    }
    return 0;
}
