#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int x;
int t;
int a[20000],n;
int main() {
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    cin >> t;
    int tk=0;
    for (;t>=1;t--) {
        cin >> n;
        for (int j=1;j<=n;j++) cin >> a[j];
        int mx=a[1];
        for (int i=1;i<=n;i++)
            if (a[i]>mx) mx=a[i];
        tk++;
        int ans=1e9;
        for (int j=1;j<=mx;j++) {
            int s=0;
            for (int i=1;i<=n;i++) {
                int y=a[i]/j;
                if ((a[i]%j)!=0) y++;
                y--;
                s+=y;
            }
            s+=j;
            if (s<ans) ans=s;
        }
        cout << "Case #" << tk << ": " << ans << "\n";
    }
    return 0;
}
