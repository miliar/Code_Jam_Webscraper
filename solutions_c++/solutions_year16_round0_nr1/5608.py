#include <bits/stdc++.h>
using namespace std;

vector<bool> count(int n){
    vector<bool> dig(10, false);
    while (n){
        dig[n%10] = true;
        n /= 10;
    }
    return dig;
}

int main(){
    int t, cases = 1;
    cin >> t;
    while (t--){
        int n;
        cin >> n;

        vector<bool> dig(10, false);

        int ans = -1;
        for (int i = 1; i <= 100; i++){
            vector<bool> aux = count(i * n);
            bool ok = true;
            for (int j = 0; j < 10; j++){
                dig[j] = dig[j] | aux[j];
                if (!dig[j])
                    ok = false;
            }
            if (ok){
                ans = i * n;
                break;
            }
        }

        cout << "Case #" << cases++ << ": ";
        if (ans == -1) cout << "INSOMNIA" << endl;
        else cout << ans << endl;
    }
    return 0;
}
