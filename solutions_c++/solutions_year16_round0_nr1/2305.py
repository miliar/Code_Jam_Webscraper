#include <iostream>

using namespace std;
using ll = long long;

int solve(const ll n){
    int seen = 0;
    for(int s = 0; s < 10000; ++s){
        ll x = s*n;
        while(x){
            seen |= 1 << (x%10);
            x /= 10;
        }
        if(seen == 1023){
            return s*n;
        }
    }
    return -1;
}

int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; ++i){
        int n;
        cin >> n;
        ll x = solve(n);
        if(x != -1){
            printf("Case #%d: %lld\n", i+1, x);
        } else {
            printf("Case #%d: INSOMNIA\n", i+1);
        }
    }
}
