#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,x,y,z; cin>>t;
    for(i=1; i<=t; i++) {
        cin>>x>>y>>z;
        if((y*z)%x) cout<<"Case #"<<i<<": "<<"RICHARD\n";
        else {
            if(x<=2) 
                cout<<"Case #"<<i<<": "<<"GABRIEL\n";
            else if(x == 3) {
                if(y*z == 3) cout<<"Case #"<<i<<": "<<"RICHARD\n";
                else cout<<"Case #"<<i<<": "<<"GABRIEL\n";
            } else {
                if(y*z == 4 || y*z == 8) cout<<"Case #"<<i<<": "<<"RICHARD\n";
                if(y*z == 12 || y*z == 16) cout<<"Case #"<<i<<": "<<"GABRIEL\n";
            }
        }
    }
    return 0;
}