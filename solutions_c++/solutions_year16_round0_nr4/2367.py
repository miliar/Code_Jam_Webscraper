#include<bits/stdc++.h>
using namespace std;

int ntest,k,c,s;

main(){
    //freopen("out.txt","w",stdout);
    cin>>ntest;
    for (int test=1;test<=ntest;test++){
        cin>>k>>c>>s;
        if (k==s){
            cout<<"Case #"<<test<<": ";
            for (int i=1;i<=k;i++) cout<<i<<" ";
            cout<<endl;
        }
    }
}
