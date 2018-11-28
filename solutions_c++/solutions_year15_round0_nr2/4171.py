#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

#define MAXN
#define LSON(x) x << 1
#define INF 0x7fffffff
#define RSON(x) x << 1 | 1
using namespace std;

typedef long long LL;
int num[2000];
priority_queue<int> que;
int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("myy.out", "w", stdout);
    int t; scanf("%d", &t);


    for(int curCase = 1; curCase <= t; curCase ++ )
    {
        //printf("case%d:\n", curCase);
        int d, cnt = 0, ans = INF;
        while(!que.empty()) {
            que.pop();
        }
        scanf("%d", &d);
        for(int i = 1; i <= d; i ++)
        {
            scanf("%d", &num[i]); //printf("%d ", num[i]);
            que.push(num[i]);
        }//printf("\n");

        while(!que.empty())
        {
            int cur = que.top();
            que.pop();
            ans = min(ans, cur+cnt);
            //printf("ans: %d\n", ans);
            if(cur == 1) break;

            if(cur == 9) {
                que.push(3);
                que.push(3);
                que.push(3);
                cnt += 2;
            }
            else {
                que.push(cur/2);
                que.push((cur+1)/2);
                cnt ++;
            }
        }
        printf("Case #%d: %d\n", curCase, ans);
    }


    return 0;
}


