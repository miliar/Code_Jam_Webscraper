#include <bits/stdc++.h>
using namespace std;

const int N = 10010;
void solve()
{
    int n,m,x;
    multiset<int> st;
    scanf("%d%d",&n,&m);
    for(int i = 1; i <= n; i ++) {
        scanf("%d",&x);
        st.insert(x);
    }
    int ans = 0;
    while(st.size() > 1) {
        multiset<int>::iterator it = st.begin();
        int x = m - (*it);
        ans ++;
        st.erase(it);
        multiset<int>::iterator iter = st.upper_bound(x);
        if(iter == st.begin()) {
            break;
        }
        iter --;
        st.erase(iter);
    }
    ans += st.size();
    cout << ans << endl;
}
    
        
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas ++) {
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}
