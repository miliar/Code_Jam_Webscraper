//
// Created by 김태우 on 2016. 4. 9..
//

#include <iostream>
#include <cstdio>
using namespace std;

#define ll long long

int digit[10];

int check(ll a) {
    while(a != 0) {
        int b = a%10;

        digit[b] = 1;
        a/=10;
    }
    int cnt = 0;
    for(int i = 0 ; i < 10 ; i++) {
        if(digit[i] == 1) cnt++;
    }

    return cnt;
}

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("answer.out", "w", stdout);

    int t;
    cin>>t;
    for(int z = 1 ; z <= t ; z++) {
        for(int i = 0 ; i < 10 ; i++) digit[i] = 0;
        ll a;
        cin>>a;

        cout<<"Case #"<<z<<": ";

        if( a == 0 ) {
            cout<<"INSOMNIA"<<endl;
        }
        else {
            ll b = 0;
            while(true) {
                b += a;
                if( check(b) == 10 ) {
                    cout<<b<<endl;
                    break;
                }
            }
        }
    }

    return 0;
}