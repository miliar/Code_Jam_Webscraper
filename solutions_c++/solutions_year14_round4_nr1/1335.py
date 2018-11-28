#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ": ";
        int n, x;
        cin >> n >> x;
        vector <int> a(n,0);
        vector <bool> b(n, true);
        for (int i=0;i<n;i++)
            cin >> a[i];
        sort(a.begin(),a.end());
        int ans = 0;
        for (int i=n-1; i>=0; i--){
            if (!b[i]) continue;
            int k = -1;
            for (int j=0;j<n;j++){
                if ((i!= j) && (b[j]) && (a[i] + a[j] <= x)){
                    k = j;
                }
            }
            if (k == -1){
                ans++;
                b[i] = false;
            }else{
                ans++;
                b[i] = false;
                b[k] = false;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
