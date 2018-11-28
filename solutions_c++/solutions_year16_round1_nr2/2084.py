#include<bits/stdc++.h>
#define ll long long
#define mp make_pair
#define pb push_back
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        int n;
        scanf("%d",&n);
        map<int,int> dp;
        for(int j=0;j<2*n-1;j++)
        {
            for(int i=0;i<n;i++)
            {
                int x;
                scanf("%d",&x);
                dp[x]++;
            }
        }
        map<int,int>:: iterator it;
        vector<int> ans;
        for(it=dp.begin();it!=dp.end();it++)
        {
            int x=it->first;
            int y=it->second;
            if(y&1) ans.pb(x);
        }
        printf("Case #%d:",c);
        for(int i=0;i<ans.size();i++)
            printf(" %d",ans[i]);
        printf("\n");
    }
return 0;
}
