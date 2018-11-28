#include <bits/stdc++.h>

using namespace std;

int a[1015];

int main()
{

    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int i, j, k;

    int t, ct = 0;

    cin >> t;

    for(k = 0;k < t; ++k){
        int n;
        cin >> n;
        for(i = 0;i < n; ++i){
            cin >> a[i];
        }
        int ans = 100000;
        int cur = 0;
        for(i = 1;i <= 1005; ++i){
            cur = 0;
            for(j = 0;j < n; ++j){
                if(a[j] > i){
                    if(a[j] % i == 0){
                        cur += (a[j] / i);
                        --cur;
                    }
                    else{
                        cur += ((a[j] / i) + 1);
                        --cur;
                    }
                }
            }
            ans = min(ans, cur + i);
        }
        printf("Case #%d: %d\n", ++ct, ans);
    }
}
