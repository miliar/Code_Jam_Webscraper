#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,cnt,arr[1100],x,ans,e = 0;
    char c;
    cin >> t;
    while(t--){
        cin >> n;
        ans = cnt = 0;
        for (int i = 0; i <= n; i++){
            cin >> c;
            x = c - '0';
            //printf("with i = %d , standing = %d, added = %d\n",i,cnt,ans);
            if (cnt >= i)
                cnt += x;
            else{
                ans += i - cnt;
                cnt += (i - cnt) + x;
            }
        }
        cout << "Case #"  << ++e << ": " << ans << endl;
    }
}
