#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("D-large.in" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t;
    cin >> t;
    for(int T=1;T<=t;T++) {
        int n;
        cin >> n;
        double a[1001] , b[1001] , c[1001];
        for(int i=0;i<n;i++) cin >> a[i];
        for(int i=0;i<n;i++) cin >> b[i];
        sort(a , a+n);
        sort(b , b+n);
        int a1 = 0 , a2 = 0;
        for(int i=0;i<n;i++) c[i] = b[i];
        for(int i=n-1;i>=0;i--) {
            for(int j=n-1;j>=0;j--) {
                if(b[j]) {
                    if(a[i] > b[j]) {
                        b[j] = 0;
                        a1++;
                        break;
                    }
                }
            }
        }
        for(int i=n-1;i>=0;i--) {
            for(int j=n-1;j>=0;j--) {
                if(a[j]) {
                    if(c[i] > a[j]) {
                        a[j] = 0;
                        a2++;
                        break;
                    }
                }
            }
        }

        cout << "Case #" << T << ": " << a1 << ' ' << n - a2 << '\n';
    }
    return 0;
}
