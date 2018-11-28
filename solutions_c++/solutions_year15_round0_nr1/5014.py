#include <bits/stdc++.h>
#define MAX_N 1010
using namespace std;

int t, n, arr[MAX_N];

int main(void) {
    if (fopen("a-small.in","r")) {
        freopen("a-small.in","r",stdin);
        freopen("a-small.out","w",stdout);
    }
    if (fopen("a-large.in","r")) {
        freopen("a-large.in","r",stdin);
        freopen("a-large.out","w",stdout);
    }
    cin >> t;
    for (int ii=1; ii<=t; ii++) {
        cin >> n;
        for (int i=0; i<=n; i++) {
            char c;
            cin >> c;
            arr[i]=c-'0';
        }
        int add=arr[0], ans=0;
        for (int i=1; i<=n; i++) {
            if (add<i) {
                ans+=i-add;
                add=i;
            }
            add+=arr[i];
        }
        cout << "Case #" << ii << ": ";
        cout << ans << "\n";
    }
    return 0;
}
