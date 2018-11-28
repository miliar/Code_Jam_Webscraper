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
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        int n;
        scanf("%d",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",cas);
            continue;
        }
        int res=(1<<10)-1;
        int i;
        for(i=1;res;i++)
        {
            int x=i*n;
            while(x)
            {
                int now=x%10;
                x/=10;
                if(res&(1<<now)) res^=(1<<now);
            }
        }
        printf("Case #%d: %d\n",cas,(i-1)*n);
    }
}
