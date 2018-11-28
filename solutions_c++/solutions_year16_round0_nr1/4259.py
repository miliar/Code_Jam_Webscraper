#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1007;

set<int> dig;
void add(int n)
{
    while (n>0)
    {
        dig.insert(n%10);
        n/=10;
    }
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    int T,n,it,ans;
    cin>>T;
    for (it=1;it<=T;it++)
    {
        cin>>n;
        cout<<"Case #"<<it<<": ";
        if (!n)
        {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        dig.clear();
        ans = 0;
        while (dig.size()<10)
        {
            ans+=n;
            add(ans);
        }
        cout<<ans<<endl;
    }

    return 0;
}
