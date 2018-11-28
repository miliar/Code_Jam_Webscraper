#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cstdlib>
#include<string>
#include<bitset>
#include<iomanip>
#include<deque>
#include<utility>
#include<functional>
#include<sstream>
#define INF 1000000000
#define fi first
#define se second
#define N 1005
#define P 1000000007
#define debug(x) cerr<<#x<<"="<<x<<endl
#define MP(x,y) make_pair(x,y)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
char s[N];
int main()
{
    int T, i, j, n, k, ans=0;
    int test = 0;
    freopen("Alarge.in","r",stdin);
    freopen("Alarge.out","w",stdout);
    cin>>T;
    while(T--)
    {
        test ++;
        ans = 0;
        printf("Case #%d: ",test);
        int flag = 0;
        scanf("%s",s+1);
        n = strlen(s+1);
        cin >> k;
        for (i = 1; i <= n-k+1; i++)
        {
            if (s[i] == '-')
            {
                ans++;
                for (j = i; j <= i+k-1; j ++)
                {
                    if(s[j]=='-')
                        s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        for (i = n-k+2; i<=n;i++)
            if(s[i]=='-')
                flag = 1;
        if(flag)
            printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}
// davidlee1999WTK 2017/
// ios::sync_with_stdio(false);
//#pragma comment(linker, "/STACK:102400000,102400000") compiler c++,not g++
/*

*/
