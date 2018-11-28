#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <stdlib.h>
#include <limits.h>


using namespace std;

typedef long long ll;


ll factor(ll t){
    ll i=2;
    while(t%i && i*i<=t) i++;
    if(t%i == 0) return i;
    else return 0;
}

ll val(string str, ll base){
    ll res = 0;
    for(int i=0; i<16; i++){
        res = (str[i] - '0') + res * base;
    }
    return res;
}

bool check(string str){
    for(ll i=2; i<=10; i++){
        ll t = val(str, i);
        ll f = factor(t);
        if(f == 0) return false;
    }
    return true;
}


int main(){
    freopen("/home/xiaodot/Downloads/in", "r", stdin);
    freopen("../out.txt", "w", stdout);
    string str = "1000000000000001";
    int n, j;
    int T;
    cin >> T;
    for(int test = 0; test < T; test++){
        cin >> n >> j;

        cout << "Case #" << test+1 << ": "<< endl;

        int cnt = 50;
        for(ll v = 32769; v < 32769 + 1000 && cnt > 0; v += 2){
            for(int i=0; i<16; i++){
                str[15-i] = ((v>>i) & 1) + '0';
            }
            if(check(str) == true) {
                cout << str;
                for(int base = 2; base <= 10; base++){
                    cout << " " << factor(val(str, base));
                }
                cout << endl;
                cnt--;
            }

        }
    }





    return 0;
}
