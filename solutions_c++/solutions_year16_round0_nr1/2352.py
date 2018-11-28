#include <iostream>

using namespace std;

typedef long long LL;

LL solve(LL n){
    if(n == 0) return -1;
    int used = 0;
    for(LL i = 1; ; ++i){
        LL v = n * i;
        while(v > 0){
            used |= (1<<(v % 10));
            v /= 10;
        }
        if(used == (1<<10)-1) return i * n;
    }
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        LL v;
        cin >> v;
        LL ans = solve(v);
        cout << "Case #" << t << ": ";
        if(ans < 0){
            cout << "INSOMNIA" << endl;
        }else{
            cout << ans << endl;
        }
    }
    return 0;
}

