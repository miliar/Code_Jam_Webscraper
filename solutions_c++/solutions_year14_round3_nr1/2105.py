#include <algorithm>
#include <vector>
#include <string>
#include <math.h>
#include <iostream>
#include <cstring>

#define ll long long

using namespace std;

const int T=2*1e2 + 5;

ll P,Q;

bool chk(ll x){
    while (x%2==0)
        x/=2;
    return (x==1);
}

int main(){
   // freopen("text.in","r",stdin);//freopen("text.out","w",stdout);
    int tests;
    cin>>tests;
    int t=tests;
    while (tests--){
        char ch;
        cin>>P>>ch>>Q;
        ll g=__gcd(P,Q);
        P/=g;
        Q/=g;
        if (!chk(Q)){
            cout<<"Case #"<<t-tests<<": "<<"impossible"<<endl;
            continue;
        }

        ll x=1;
        ll ans=0;
        while ( P*x < Q )
            x*=2ll,ans++;
        cout<<"Case #"<<t-tests<<": "<<ans<<endl;
    }
    return 0;
}