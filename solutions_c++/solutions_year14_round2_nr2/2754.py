#include<bits/stdc++.h>
using namespace std;
int main()
{
        freopen("B-small-attempt0.in","r",stdin);
        freopen("out.txt","w",stdout);
        int t , a , b , k;
        cin >> t;
        for(int T=1;T<=t;T++) {
                cin >> a >> b >> k;
                long long ans = 0;
                for(int i=0;i<a;i++) {
                        for(int j=0;j<b;j++) {
                                if((i&j) < k) ans++;
                        }
                }
                cout << "Case #" << T << ": " << ans << '\n';
        }
        return 0;
}
