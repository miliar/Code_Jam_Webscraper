#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll solve(ll n){
    set<int> s;
    for(int i = 1;; i++){
        ll x = n*i;
        while(x){
            s.insert(x%10);
            x/=10;
        }
        if(s.size() == 10){
            return n*i;
        }
    }
}

int main(){
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        int n;
        scanf("%d", &n);
        if(n == 0){printf("Case #%d: INSOMNIA\n", i);}
        else{printf("Case #%d: %d\n", i, solve(n));}
    }
    return 0;
}
