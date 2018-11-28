#include <bits/stdc++.h>
using namespace std;
int cake[1005];
int main(){
    freopen("InfiniteHouseofPancakes.in", "r", stdin);
    freopen("InfiniteHouseofPancakes.out", "w", stdout);
    int i, j, k, t, n, Case=1, Max;
    char ch;
    cin >> t;
    while(t--){
        cin >> n;
        Max = -1;
        for(i=0;i<n;i++)
            cin >> cake[i], Max = max(Max,cake[i]);

        int res = INT_MAX;
        for(i=1;i<=Max;i++){
            int cnt = 0;
            for(j=0;j<n;j++){
                int x = cake[j];
                if(x%i==0) cnt+=x/i-1;
                else cnt+= x/i;
            }
            res = min(res,cnt+i);
        }

        cout << "Case #" << Case++ << ": " << res << endl;
    }

return 0;

}

