#include <bits/stdc++.h>
using namespace std;

int main(){
    int T;
    cin >> T;
    for(int casos = 1; casos <= T; casos++){
        int n, res = 0;
        string audiencia;
        cin >> n >> audiencia;
        int acumulados = audiencia[0] - 48;
        for(int i = 1; i <= n; i++){
            if(audiencia[i] - 48 == 0) continue;
            if(acumulados >= i){
                acumulados += audiencia[i] - 48;
            } else {
                res += i - acumulados;
                acumulados += i - acumulados + (audiencia[i] - 48);
            }
        }
        cout << "Case #" << casos << ": " << res << "\n";
    }
    return 0;
}
