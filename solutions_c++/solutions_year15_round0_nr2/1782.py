//#pragma comment(linker,"/STACK:102400000,102400000")
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<string>
#define ll long long
#define db double
#define PB push_back
#define lson k<<1
#define rson k<<1|1
using namespace std;

const int N = 1005;

int p[N];

int main()
{
#ifdef PKWV
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out","w",stdout);
#endif // PKWV
    int T, cas(1);
    scanf("%d", &T);
    while(T--)
    {
        int d;
        scanf("%d", &d);
        int h = 0;
        for(int i = 0; i < d; i++) scanf("%d", &p[i]), h = max(h, p[i]);
        int res = h;
        for(int i = 1; i <= h; i++)
        {
            int cnt(0);
            for(int j = 0; j < d; j++)
            {
                cnt += (p[j] + i - 1) / i-1;
            }
            cnt+=i;
            res = min(res, cnt);
        }
        printf("Case #%d: %d\n", cas++, res);
    }
    return 0;
}
