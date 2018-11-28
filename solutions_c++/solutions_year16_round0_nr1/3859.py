#include <bits/stdc++.h>

using namespace std;

#define ll long long

bool has;
ll T, a, tmp = 0;
int b[10] = {0};
void add(ll a){
    while(a){
        if(b[a%10] == 0){
            b[a%10] = 1;
            tmp++;
        }
        a = a/ 10;
    }
}
int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    cin>>T;
    for(int t = 1; t <= T; ++t){
        cin>>a;
        cout<<"Case #"<<t<<": ";
        tmp = 0;
        has = false;
        memset(b, 0, 10*4);
        for(ll i = 1; i < 1000; ++i){
            add(a*i);
            if(tmp == 10){
                cout<<a*i<<endl;
                has = true;
                break;
            }
        }
        if(!has){
            cout<<"INSOMNIA\n";
        }
    }
    return 0;
}
