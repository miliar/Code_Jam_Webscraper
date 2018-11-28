#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long t, k, c, s;
    cin >> t;
    for(int z = 1;z <= t;z++){
        cin >> k >> c >> s;
        cout << "Case #" << z << ": ";
        if(s < k){
            cout << "IMPOSSIBLE" << endl;
        }
        else{
            for(int i = 0;i < k - 1;i++){
                cout << i + 1 << " ";
            }
            cout << k << endl;
        }
    }
    return 0;
}
