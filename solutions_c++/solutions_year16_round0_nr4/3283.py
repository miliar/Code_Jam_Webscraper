#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    freopen("INP.txt","r+",stdin);
    freopen("ANS.txt","w+",stdout);
    int t,i=1,K,C,S;

    for(cin>>t;i<=t;i++){
        cin>>K>>C>>S;
        ll num=1;
        ll inc=pow(K,C-1);
        cout<<"Case #"<<i<<": ";
        while(S--){
            cout<<num<<" ";
            num+=inc;
        }
        cout<<endl;
    }
    return 0;
}
