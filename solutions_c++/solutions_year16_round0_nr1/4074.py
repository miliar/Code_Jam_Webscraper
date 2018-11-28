#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
using namespace std;
int a[10];

void solve()
{
    int T,kcase = 1;
    cin>>T;
    while(T--)
    {
        memset(a,0,sizeof a);
        int n,cnt = 0;
        long long ans;
        scanf("%d",&n);
        for(int i = 1; n ; ++i)
        {
            long long tp = 1LL * i * n;
            while(tp)
            {
                if(a[tp % 10] == 0)
                {
                    a[tp % 10] = 1;
                    cnt++;
                }
                tp /= 10;
            }
            if(cnt == 10)
            {
                ans = 1LL * i * n;
                break;
            }
        }
        printf("Case #%d: ",kcase++);
        if(n == 0) printf("INSOMNIA\n");
        else cout << ans << endl;
    }
}

int main() {
    freopen("in","r",stdin);
    freopen("A.out","w",stdout);
    solve();
    return 0;
}
