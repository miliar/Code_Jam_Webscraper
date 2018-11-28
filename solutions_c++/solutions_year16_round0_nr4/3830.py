#include <bits/stdc++.h>
using namespace std;
int main(){
    int T,K,C,S;
    cin>>T;
    for(int l=0;l<T;l++){
        cin>>K>>C>>S;
        cout<<"Case #"<<l+1<<":";
        for(int i=1;i<=S;i++){
            cout<<" "<<i;
        }
        cout<<endl;
    }
    return 0;
}
