#include <bits/stdc++.h>
using namespace std;
#define ULL unsigned long long
bool visited[10];

int main()
{
//    freopen("A-large.in", "r", stdin);
//    freopen("out.txt", "w",  stdout);
    int t,qq=1;
    scanf("%d",&t);
    while(t--)
    {
        ULL n,ans,tmp;
        scanf("%llu",&n);
        printf("Case #%d: ",qq++);
        if(!n)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int done = 10;
        ans = 0;
        memset(visited,false,sizeof(visited));
        while(done)
        {
            ans += n;
            tmp = ans;
            while(tmp)
            {
                int r = tmp%10;
                if(!visited[r]) visited[r] = true , done--;
                tmp/=10;
            }
        }
        printf("%llu\n",ans);
    }
    return 0;
}
