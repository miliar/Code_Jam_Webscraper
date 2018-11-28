//
//  main.cpp
//  Coin Jam
//
//  Created by Nabil SHF on 4/9/16.
//  Copyright © 2016 Nabil SHF. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
using namespace std;

typedef long long int ll;
int n, counter, cpt;
string token;
ll dive[13];

ll divisor(string s, int base){
    int n = (int)s.size();
    ll res = 0;
    ll a = 1;
    for (int i=n-1;i>=0;i--){
        res += (a*(s[i]-'0'));
        a = a*base;
    }
    
    for (ll i=2;i*i<=res+2;++i){
        if (res%i==0){
            return i;
        }
    }
    return -1;
}

void backtrack(int idx){
    if (idx == n-1){
        int j = 2;
        bool isOk = true;
        for (int base = 2;base<=10;++base){
            ll d = divisor(token, base);
            if (d != -1){
                dive[j++] = d;
            }
            else{
                isOk = false;
                break;
            }
        }
        if (isOk && cpt<counter){
            cout<<token;
            for (int i = 2;i<=10;++i) cout<<" "<<dive[i];
            cout<<endl;
            cpt++;
        }
        return;
    }
    
    token[idx] = '0';
    backtrack(idx+1);
    token[idx] = '1';
    backtrack(idx+1);
    return;
}

int main(){
    int t;
    scanf ("%d",&t);
    for (int l = 1;l<=t;++l){
        scanf ("%d %d",&n,&counter);
        cpt = 0;
        printf ("Case #%d:\n",l);
        token.resize(n);
        token[0] = '1';
        token[n-1] = '1';
        backtrack(1);
    }
    return 0;
}