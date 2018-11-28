#include<bits/stdc++.h>
using namespace std;
#define ll long long int


int main()
{
    ll t,k,c,s;
    scanf("%lld", &t);
    for(int i=1; i<=t;i++) {
        scanf("%lld %lld %lld",&k,&c,&s);

        cout<<"Case #"<<i<<": ";

        if(s<k) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        for(ll j=1;j<=s;j++)
            cout<<j<<" ";
        cout<<"\n";
    }
    return 0;
}
