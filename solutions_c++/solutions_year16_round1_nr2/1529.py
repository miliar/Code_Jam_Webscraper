#include<bits/stdc++.h>


using namespace std;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("B-large.in","r",stdin);
    freopen("Blargeout.out","w",stdout);

    int t,i,j,k,x,n;
    vector<int> ans;
    vector<int> m;
    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        m.resize(2510,0);
        scanf("%d",&n);
        for(j=1;j<=2*n-1;++j)
        {
            for(k=1;k<=n;++k)
            {
                scanf("%d",&x);
                m[x]++;
            }
        }
        for(j=1;j<=2500;++j)
            if(m[j]&1)
                ans.push_back(j);
        sort(ans.begin(),ans.end());
        printf("Case #%d: ",i);
        for(j=0;j<ans.size();++j)
            printf("%d ",ans[j]);
        printf("\n");
        ans.clear();
        m.clear();
    }
    return 0;
}
