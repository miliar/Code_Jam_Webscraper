#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
int v[10];
int main(){
    int t;
    ll N;
    cin >> t;
    for(int i = 1; i <= t; i++){
        cin >> N;
        if(N == 0){
            cout << "Case #" << i << ": INSOMNIA" << endl;
        } else {
            memset(v, 0, sizeof(v));
            for(int x = 1; x < 1000; x++){
                ll ans = 1ll * N * x;
                ll n = ans;
                while(n > 0){
                    v[ n % 10 ]++;
                    n /= 10;
                }
                bool check = true;
                for(int y = 0; y < 10 && check; y++){
                    if(!v[y])
                        check = false;
                }
                if(check){
                    cout << "Case #" << i << ": " << ans << endl;
                    break;
                }
            }
        }
    }
    return 0;
}
