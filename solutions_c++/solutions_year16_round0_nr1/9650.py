#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

bool check(vector<bool>& d){
    for(auto di : d) if(not di) return false;
    return true;
}

void mark(vector<bool>& d, ll x){
    while(x){
        d[x % 10ll] = true;
        x /= 10ll;
    }
}

ll f(ll n){
    ll x = 0;
    int its = 0;
    vector<bool> d(10);
    do{
        x += n;
        mark(d, x);
        its++;
    }while(not check(d) and its < 1000000);

    return check(d) ? x : -1;
}

int main(){
    int T;
    cin >> T;
    for(int tc = 1; tc <= T; tc++){
        ll n;
        cin >> n;
        cout << "Case #" << tc << ": ";
        ll sol = f(n);
        if(sol == -1){
            cout << "INSOMNIA";
        }else{
            cout << sol;
        }
        cout << '\n';
    }
}
