#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("E:\\acm\\input.txt","r",stdin);
    freopen("E:\\acm\\output.txt","w",stdout);
    int T; cin>>T;
    for(int cas=1; cas<=T; cas++)
    {
        int a,ans = 0 ,rec = 0;
        cin>>a;
        int cnt[20] = {0};
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
            {
                int tmp; cin>>tmp;
                if(i == a)
                    cnt[tmp]++;
            }
        cin>>a;
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
            {
                int tmp; cin>>tmp;
                if(i == a)
                    cnt[tmp]++;
            }
        for(int i=1; i<=16; i++) if(cnt[i] == 2)
        {
            ans ++;
            rec = i;
        }
        printf("Case #%d: ",cas);
        if(ans == 1) printf("%d\n",rec);
        else if(ans >= 2) printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }
}
