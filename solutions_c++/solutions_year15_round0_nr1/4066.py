#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

int num[1010];

int main()
{
    int t;
//    freopen("a.in","r",stdin);
//    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for(int Case=1;Case<=t;Case++)
    {
        int large;
        char s[1010];
        scanf("%d%s",&large,s);
        for(int i=0;i<=large;i++)
        {
            num[i]=s[i]-'0';
        }
        int cnt=num[0];
        int ans=0;
        for(int i=1;i<=large;i++)
        {
            //cout<<sum<<ends<<cnt<<ends<<ans<<endl;
//            if(num[i]==0)
//                continue;
            if(cnt>=i)
            {
                cnt+=num[i];
            }
            else
            {
                ans+=i-cnt;
                cnt+=num[i]+i-cnt;
            }
        }
        printf("Case #%d: %d\n",Case,ans);
    }
    return 0;
}
