#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <stack>
#include <queue>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define LL long long
#define PI 3.1415926535897932626
using namespace std;
int gcd(int a, int b) {return a % b == 0 ? b : gcd(b, a % b);}
int cnt[20];
int main()
{
       //freopen("A-small-attempt2.in","r",stdin);
        //freopen("output.in","w",stdout);
        int T,kase = 1;
        scanf("%d",&T);
        while (T--)
        {
                int N;
                scanf("%d",&N);
                char str[20];
                scanf("%s",str);
                for (int i = 0 ; i <= N ; i++) cnt[i] = str[i] - '0';
                int cur = cnt[0],ans = 0;
                for (int i = 1; i <= N; i++)
                {
                        if (cnt[i] == 0) continue;
                        if (i > cur)
                        {
                                ans += i - cur;
                                cur = cur + ans + cnt[i];
                        }
                        else cur = cur + cnt[i];
                }
                printf("Case #%d: %d\n",kase++,ans);
        }
        return 0;
}
