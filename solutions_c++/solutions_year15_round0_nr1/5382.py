#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int idx=1;
    while(t--)
    {
        int n;
        scanf("%d",&n);
        char str[n+10];
        cin>>str;
        int alreadyStanding[n+10];
        int ans=0;
        alreadyStanding[0]=str[0]-'0';
        for(int i=1;i<=n;i++)
        {
            alreadyStanding[i]=alreadyStanding[i-1];
            if(alreadyStanding[i]<i && (str[i]-'0')>0)
            {
                ans+=i-alreadyStanding[i];
                alreadyStanding[i] += i-alreadyStanding[i];
            }
            alreadyStanding[i] += str[i]-'0';
            //cout<<"\n"<<ans<<" "<<alreadyStanding[i];
        }
        printf("Case #%d: %d\n",idx,ans);
        ++idx;
    }
    return 0;
}
