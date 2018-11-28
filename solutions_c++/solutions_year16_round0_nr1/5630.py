#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int mx;


ll f(ll x){
    set<int> nu;
    int it = 1;
    while(nu.size() != 10){
        ll tx = x * it;
        while(tx){
            nu.insert(tx % 10);
            tx /= 10;
        }    
        it++;    
        
    }

    return x * (it - 1);

}

int main(){
    int t,nc = 0; cin >> t;
    while(t--){
        ll x; cin >> x;
        cout << "Case #" << ++nc << ": ";
        if(x == 0) cout << "INSOMNIA" << endl;
        else       cout << f(x) << endl;
    }
    
}
