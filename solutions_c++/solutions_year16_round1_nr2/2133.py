#include <bits/stdc++.h>
using namespace std;
int cnt[2510];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int test=1;test<=t;test++)
    {
        int n;
        cin >> n;
        for(int i=1;i<=2500;i++) cnt[i]=0;
        for(int i=0;i<n*(2*n-1);i++)
        {
            int foo;
            scanf("%d",&foo);
            cnt[foo]++;
        }
        vector<int> ans;
        cout << "Case #" << test << ": ";
        for(int i=1;i<=2500;i++) if(cnt[i]&1) ans.push_back(i);
        assert(ans.size()==n);
        for(int i=0;i<n;i++) printf("%d ",ans[i]);
        printf("\n");
    }
}
