#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>

#define rep(i,n) for (int n__=n,i=1;i<=n__;i++)
using namespace std;
typedef long long LL;
const int mN=10000+50;

multiset<int> a;

int main()
{
    freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
    int ta;
    cin>>ta;
    rep(tz,ta)
    {
        a.clear();
        printf("Case #%d: ",tz);
        int n,cap;
        cin>>n>>cap;
        rep(i,n)
        {
            int bu;
            cin>>bu;
            a.insert(bu);
        }
        int ans=0;
        while (!a.empty())
        {

            ans++;
            multiset<int>::iterator it=a.end();
            it--;
            int x=*it;
            a.erase(it);
            it=a.upper_bound(cap-x);
            if (it!=a.begin())
            {
                it--;
                a.erase(it);
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
