#include <bits/stdc++.h>
typedef __int128 INT;
typedef INT Int;

typedef long long LL;
using namespace std;

istream& operator>>(istream& is,INT x){
    LL _x;is>>_x;x=_x;return is;
}
ostream& operator<<(ostream& os,INT x){
    os<<(LL)x;return os;
}

#define pos(b,k) (1ll&(b>>k))
int getdivisor(INT x){
    for(int i = 2; i < min((INT)1000,x); i++)
        if(x%i==0)return i;
    return 0;
}
inline bool check(LL x,int n){
    for(int d = 2; d <= 10; d++){
        INT D=1,y=0;
        for(int i = 0; i < n; i++,D*=d){
            if(pos(x,i))y+=D;
        }
        if(getdivisor(y)==0)return false;
    }
    return true;
}
inline void print(LL x,int n){
    for(int d = 2; d <= 10; d++){
        INT D=1,y=0;
        for(int i = 0; i < n; i++,D*=d){
            if(pos(x,i))y+=D;
        }
        //cout<<" "<<y<<"/"<<getdivisor(y)<<"="<<y/getdivisor(y)<<":"<<y%getdivisor(y);
        cout<<" "<<getdivisor(y);
    }
}
void solve(){
    int N,J;
    cin>>N>>J;
    set<LL> res;
    LL mask=(1ll<<(N-2))-1;

    while((int)res.size()<J){
        LL test=rand()&mask;
        //for(int i = 0; i < N-2; i++)cout<<pos(test,i);cout<<endl;
        test|=mask+1;
        test<<=1;
        test|=1;
        //for(int i = 0; i < N; i++)cout<<pos(test,i);cout<<endl;
        if(res.count(test))continue;
        if(check(test,N))res.insert(test);
    }
    for(auto& it : res){
        for(int i = N-1; i >= 0; i--)cout<<pos(it,i);
        print(it,N);
        cout<<endl;
    }
}

int main() {
    int T;cin>>T;
    for(int i = 1; i <= T; i++){
        cout<<"Case #"<<i<<": "<<endl;
        solve();
    }

    return 0;
}
