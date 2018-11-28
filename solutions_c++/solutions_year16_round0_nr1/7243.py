#include <bits/stdc++.h>

using namespace std;
#define ll long long
int main(){

    freopen("A-large.in", "r", stdin);

    freopen("op.txt", "w",stdout);

    ll t, n, i;

    cin>>t;

    for(i=1; i<=t; i++){

        cin>>n;

        ll x[11];

        int p=0;

        memset(x, 0, sizeof(x));

        ll c=n;

        ll d=1;

        if(n==0)printf("Case #%lld: INSOMNIA\n",i);
        else{
        while(1){

            c=n*d;

            while(c){

                if(x[c%10]==0){
                    x[c%10]=1;

                    p++;

                }

                c/=10;

            }


            if(p==10)break;

            d++;

        }

        printf("Case #%lld: %lld\n", i, n*d);

        }
    }

}
