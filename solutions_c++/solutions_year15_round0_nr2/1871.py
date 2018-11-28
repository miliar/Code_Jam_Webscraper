#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<queue>
#include<stack>
#include<set>
#include<cmath>
#include<vector>
#include<bitset>
#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define eps 1e-6
#define pi acos(-1.0)
using namespace std;
typedef long long ll;
const int maxn = 1000 + 10;
int P[maxn];
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int t,tcase = 0;
    scanf("%d",&t);
    while(t--) {
        tcase++;
        int n,m = 0;
        scanf("%d",&n);
        for (int i = 0;i < n;++i) {
            scanf("%d",&P[i]);
            m = max(m ,P[i]);
        }
        sort(P,P + n);
        int ans = inf;
        for(int i = 1;i <= m;++i) {
            int sum = 0;
            for(int j = n - 1;j >= 0;--j) {
                if(P[j] > i) {
                    sum += (P[j] - 1)/i;
                }
                else break;
            }
            ans = min(ans, sum + i);
        }
        printf("Case #%d: %d\n",tcase,ans);
    }
    return 0;
}
