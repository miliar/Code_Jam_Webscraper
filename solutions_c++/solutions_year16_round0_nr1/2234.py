#include <bits/stdc++.h>
typedef __int128 INT;
typedef long long LL;
using namespace std;

istream& operator>>(istream& is,INT& x){
    LL _x;is>>_x;x=_x;return is;
}
ostream& operator<<(ostream& os,INT& x){
    os<<(LL)x;return os;
}
using namespace std;
void solve(){
    INT x;
    cin>>x;
    if(x==0){
        cout<<"INSOMNIA";
        return;
    }
    int exist=0;
    int finish=(1<<10)-1;
    INT y = x;
    for(x=0; exist != finish; ){
        x+=y;
        INT z=x;
        while(z){
            exist|=1<<(z%10);
            z/=10;
        }
    }
    cout<<x;
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
