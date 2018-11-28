#include <bits/stdc++.h>

#define FOR(i,n) for(int i=0;i<n;++i)

using namespace std;

bool szj[10];

bool good(){
    FOR(i,10) if(szj[i]==false) return false;

    return true;
}

void solve(long long x){
    if(x==0){cout<<"INSOMNIA"<<endl;return;}
    FOR(i,10) szj[i]=false;

    long long xx;

    int i=0;
    while(!good()){
        ++i;
        xx=i*x;
        while(xx!=0){
            szj[xx%10]=true;
            xx/=10;
        }
    }

    cout<<i*x<<endl;
}

int main(void){
    long long t; cin>>t;
    FOR(i,t){
        long long n; cin>>n;
        cout<<"Case #"<<i+1<<": ";
        solve(n);
    }
}
