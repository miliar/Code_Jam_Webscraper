#include <bits/stdc++.h>

using namespace std;
typedef long long  ll;


int main()
{
    freopen("ini.txt","r",stdin);
    freopen("filla.txt","w",stdout);
    int t;
    cin>>t;
    for (int z = 1; z<t+1; z++) {
        ll n ;
        cin>>n;
        int occ[10];
        memset(occ, 0, sizeof(occ));
        ll sol=-1;
        for (int i = 1; i<1000;i++) {
            ll temp  = n *i ;
            while (temp) {
                occ[temp%10]++;
                temp/=10;
            }
            ll prod=1;
            for (int j=0; j<10; j++) {
                prod=prod*occ[j];
            }
            if (prod!=0) {
                sol=n*i;
                break;
            }
        }
        
        if (sol==-1) {
            cout<<"Case #"<<z<<": INSOMNIA";
        }
        else         cout<<"Case #"<<z<<": "<<sol;
        cout<<endl;
        
    }
    
    
    return 0 ;
}