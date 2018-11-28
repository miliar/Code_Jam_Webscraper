#include<bits/stdc++.h>

typedef long long lld;
using namespace std;
int a[1010];
int main()
{
    freopen("in1.in","r",stdin);
    freopen("out1.out","w",stdout);
    int t,n,j,i,cas = 0;
    cin>>t;
    while(t--)
    {
        cas++;
        printf("Case #%d: ",cas);
        cin>>n;
        int ans = 0, dif = -1;
        cin>>a[1];
        for( i = 2;i <= n; i++) {
            cin>>a[i];
            if(a[i] < a[i-1]) {
                ans += (a[i-1] - a[i]);
                if ((a[i-1] - a[i]) > dif) dif = (a[i-1] - a[i]);
            }
        }
        cout<<ans<<" ";
        ans = 0;
        if( dif == -1 ) {
            cout<<"0\n";continue;
        }
        for( i = 1;i <= n-1; i++) {
            if(a[i] >= dif) ans += dif;
            else ans += a[i];
        }
        cout<<ans<<endl;
    }
}
