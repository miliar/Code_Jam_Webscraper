#include <iostream>
#include <stdio.h>
using namespace std;
int tt;
void solve()
{
    string st;
    int t;cin >> t;
    cin >> st;
    int len = st.length();
    int curr = 0;
    int ans = 0;
    for(int i=0;i<len;i++)
    {
        if(curr >= i) curr += st[i]-'0';
        else
        {
            ans = ans + (i-curr);
            curr = i + st[i]-'0';
        }
    }
    cout << "Case #" << tt << ": " << ans <<endl;
}
int main()
{
    int t;
    //freopen ("A-small-attempt0.in","r",stdin);
    //freopen ("out.txt","w",stdout);
    cin >> t;
    for(tt = 1;tt <= t;tt++)
    {
        solve();
    }
}
