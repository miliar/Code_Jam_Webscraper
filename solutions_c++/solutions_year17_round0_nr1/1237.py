#include<bits/stdc++.h>
using namespace std;
int n,k;
char s[1005];
main()
{
    int time,cnum=1;
    int i,j,cnt,ans;
    freopen("A-large.in","r",stdin);
    freopen("A_out.txt","w",stdout);
    scanf("%d",&time);
    while(time--)
    {
        scanf(" %s%d",s,&k);
        n = strlen(s);
        cnt = 0;
        for(i=0;i<=n-k;i++)
        {
            if(s[i]=='-')
            {
                for(j=0;j<k;j++)
                {
                    if(s[i+j]=='+') s[i+j] = '-';
                    else s[i+j] = '+';
                }
                cnt++;
            }
        }
        ans = 1;
        for(i=0;i<n;i++) if(s[i]=='-') ans = 0;
        if(!ans) printf("Case #%d: IMPOSSIBLE\n",cnum++);
        else printf("Case #%d: %d\n",cnum++,cnt);
    }
}
