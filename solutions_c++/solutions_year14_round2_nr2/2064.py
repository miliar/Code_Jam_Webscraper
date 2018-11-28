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
        int a, b, k;
        cin >> a >> b >> k;
        int ans=0;
        for (int i=0;i<a;i++){
            for (int j=0;j<b;j++){
                if ((i & j) < k) ans++;
            }
        }
        cout << ans << endl;
    }

    return 0;
}
