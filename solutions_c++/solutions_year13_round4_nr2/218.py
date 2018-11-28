#include <iostream>
using namespace std;
typedef long long ll;
ll sure(ll n, ll p){
    if (p<=(1LL<<(n-1)))
        return 0;
    else{
        ll k = sure(n-1, p-(1LL<<(n-1)));
        return min(2*k+2,(1LL<<n)-1);
    }
}
ll could(ll n, ll p){
    if (p>=(1LL<<n))
        return (1LL<<n)-1;
    if (p>=(1LL<<(n-1)))
        return (1LL<<n)-2;
    ll k=could(n-1, p);
    return min(2*k,(1LL<<n)-1);
}
int main(){
    int tcou;cin>>tcou;int tnum=0;
    while (tcou--){
        ll n, p;
        cin>>n>>p;
        cout<<"Case #"<<(++tnum)<<": "<<sure(n, p)<<' '<<could(n, p)<<endl;
    }
    return 0;
}
