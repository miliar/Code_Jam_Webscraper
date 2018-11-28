#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<cstdlib>
using namespace std;
typedef long long ll;

int T, cas;
int n, sum, res;
char s[10010];

int main()
{
//    freopen("A-large.in", "r", stdin);
//    freopen("out.out", "w", stdout);
    scanf("%d", &T);
    for(cas = 1; cas <= T; cas++)
    {
        sum = 0;
        res = 0;
        scanf("%d", &n);
        scanf("%s", &s);
        for(int i = 0; i <= n; i++)
        {
            if(sum >= i)
            {
                sum += (s[i] - '0');
            }
            else
            {
                res += (i - sum);
                sum = i + s[i] - '0';
            }
        }
        printf("Case #%d: %d\n", cas, res);
    }
    return 0;
}
