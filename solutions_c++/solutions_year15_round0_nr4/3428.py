#include <bits/stdc++.h>
using namespace std;
int main(){
    int t,x,r,c;
    cin>>t;
    for (int i = 0; i < t; i++) {
        cin>>x>>r>>c;
        if(x!=6&&x>(max(r,c))||min(r,c)<x-1){
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
        }
        else if((r*c)%x==0){
            cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
        }
        else{
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
        }
    }
    return 0;
}