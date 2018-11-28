#include <bits/stdc++.h>
typedef __int128 INT;
typedef long long LL;
using namespace std;

istream& operator>>(istream& is,INT& x){LL _x;is>>_x;x=_x;return is;}
ostream& operator<<(ostream& os,INT& x){os<<(LL)x;return os;}
void solve(){
    int K,C,S;
    cin>>K>>C>>S;
    for(int i = 0; i < K; i++)
        cout<<(!i)+" "<<i+1;
}

int main() {
    int T;cin>>T;
    for(int i = 1; i <= T; i++){
        cout<<"Case #"<<i<<": ";
        solve();
        cout<<endl;
    }

    return 0;
}
