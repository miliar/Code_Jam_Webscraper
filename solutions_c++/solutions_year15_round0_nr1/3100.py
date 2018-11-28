#include<bits/stdc++.h>
using namespace std;
char str[1105];
int main()
{
    int T;
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    int N,i,it;
    for(it=1; it<=T; it++)
    {
        scanf("%d",&N);
        scanf("%s",str);
        int cnt=0;
        int ans=0;
        for(i=0; i<=N; i++)
        {
            if(cnt<i)
            {
                ans+=(i-cnt);
                cnt=i;
            }
            cnt+=str[i]-'0';
        }
        printf("Case #%d: %d\n",it,ans);
    }
    return 0;
}
