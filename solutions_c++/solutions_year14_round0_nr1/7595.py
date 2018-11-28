#include<bits/stdc++.h>

using namespace std;
int cnt,n,a,b,c,d,i,t,l,ans;
map<int,int>mp;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        mp.clear();
        cnt=0;
        scanf("%d",&n);
        for(i=1;i<=4;i++)
        {
            scanf("%d %d %d %d",&a,&b,&c,&d);
            if(i==n)
            {
                mp[a]++;
                mp[b]++;
                mp[c]++;
                mp[d]++;
            }
        }
        scanf("%d",&n);
        for(i=1;i<=4;i++)
        {
            scanf("%d %d %d %d",&a,&b,&c,&d);
            if(i==n)
            {
                mp[a]++;
                mp[b]++;
                mp[c]++;
                mp[d]++;
            }
        }
        for(i=1;i<=16;i++)
        {
            if(mp[i]>0)
            {
                cnt++;
            }
            if(mp[i]==2)
            {
                ans=i;
            }
        }
        printf("Case #%d: ",l);
        if(cnt==7)
        {
            printf("%d\n",ans);
        }
        else if(cnt==8)
        {
            printf("Volunteer cheated!\n");
        }
        else
        {
            printf("Bad magician!\n");
        }
    }
    return 0;
}
