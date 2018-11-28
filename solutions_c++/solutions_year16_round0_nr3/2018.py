#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
bool isv(ll n){
    ll cur = 1;
    int f = 0, s = 0;
    for(int i=0; i<40; i+=2){
        if(n & cur) f++;
        cur *= 4LL;
    }
    cur = 2;
    for(int i=1; i<40; i+=2){
        if(n & cur) s++;
        cur *= 4LL;
    }
    return (f == s);
}
main(){
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        cout << "Case #" << i + 1 << ": " << endl;
        vector<ll>jav;
        int a, b;
        cin >> a >> b;
        ll mask = ((1LL) <<  (a - 1) ) + 1;
        while(jav.size() < b){
            if(isv(mask)) jav.push_back(mask);
            mask += 2;
        }
        for(ll mask : jav){
            for(int j = a - 1; j >= 0; j--){
                if(mask & (1<<j))
                    cout << "1";
                else
                    cout << "0";
            }
            cout << " ";
            for(int k=2; k<=10; k++)
                cout << k + 1 << " ";
            cout << endl;
        }
    }
}
