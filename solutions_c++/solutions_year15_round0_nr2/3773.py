#include <bits/stdc++.h>
using namespace std;

int pancake[1002];

int main(){
    int T;
    cin >> T;
    for(int casos = 1; casos <= T; casos++){

        int n;
        cin >> n;
        for(int i = 0; i < n; i++)
            cin >> pancake[i];

        int res = (1 << 30);
        for(int k = 1; k <= 1000; k++){
            int query = 0;
            for(int i = 0; i < n; i++) query += (pancake[i] - 1) / k;
            res = min(res, query + k);
        }

        cout << "Case #" << casos << ": " << res << "\n";
     }
    return 0;
}
