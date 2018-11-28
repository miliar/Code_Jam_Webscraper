#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <set>

using namespace std;

string broj;
set<char> S;

string Add(string prvi, string drugi){
    if((int)prvi.length() == 0) return drugi;
    if((int)drugi.length() == 0) return prvi;
    while((int)drugi.length() < (int)prvi.length()) drugi.insert(drugi.begin(), '0');
    int carry = 0;
    string ret = "";
    for(int i = (int)prvi.length() - 1; i >= 0; i--){
        int sada = (drugi[i] - '0') + (prvi[i] - '0') + carry;
        ret.insert(ret.begin(), (char)(sada % 10 + '0'));
        carry = sada / 10;
    }
    while(carry){
        ret.insert(ret.begin(), (char)(carry % 10 + '0'));
        carry /= 10;
    }

    return ret;
}

int main(){
    freopen("veliki.in", "r", stdin);
    freopen("output", "w", stdout);

    int t;
    cin >> t;

    for(int tt = 1; tt <= t; tt++){
        cin >> broj;

        if(broj == "0"){
            cout << "Case #" << tt << ": ";
            cout << "INSOMNIA" << endl;
            continue;
        }

        S.clear();

        string sum = broj;
        for(int i = 0; i < 100; i++){
            for(int j = 0; j < (int)sum.length(); j++) S.insert(sum[j]);
            if((int)S.size() == 10) break;
            sum = Add(sum, broj);
        }

        cout << "Case #" << tt << ": " << sum << endl;
    }

    return 0;
}
