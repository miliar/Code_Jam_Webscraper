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
char S[maxn];
int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);
    int T,tcase = 0;
    scanf("%d",&T);
    while(T--) {
        tcase ++;
        int n;
        scanf("%d",&n);
        scanf("%s",S);
        int ans = 0, sum = 0;
        for (int i = 0;i <= n;++i) {
            int val = S[i] - '0';
            if (sum >= i) {
                sum += val;
            }
            else {
                ans += (i - sum);
                sum += val + (i - sum);
            }
        }
        printf("Case #%d: %d\n",tcase,ans);
    }
    return 0;
}
