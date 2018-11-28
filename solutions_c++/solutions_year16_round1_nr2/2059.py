#include <bits/stdc++.h>
#define MAXA 100005
#define MOD 1000000007
using namespace std;
int c[2555];
vector<int> ans;
int main()
{
    freopen("B-large.in","r+",stdin);
    freopen("output1.txt","w+",stdout);
    int t,i,n,j,x,t1=1;
    cin>>t;
    while(t--)
    {
        ans.clear();
        int maxa=0;
        memset(c,0,sizeof(c));
        cin>>n;
        for(i=0;i<2*n-1;i++)
        {
            for(j=0;j<n;j++)
            {
                cin>>x;
                c[x]++;
                maxa=max(maxa,x);
            }
        }
        for(i=1;i<=maxa;i++)
        {
            if(c[i]!=0&&c[i]%2!=0)
                ans.push_back(i);
        }
        printf("Case #%d:",t1);
        for(i=0;i<ans.size();i++)
            printf(" %d",ans[i]);
        t1++;
        printf("\n");
    }
    return 0;
}
