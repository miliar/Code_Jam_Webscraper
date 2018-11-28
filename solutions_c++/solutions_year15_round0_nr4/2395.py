#include<iostream>
using namespace std;

int main () {

    int t;
    cin>>t;
    for (int i=1;i<=t;i++){
        int x,r,c;
        cin>>x>>r>>c;

        if (x==1){
            cout<<"Case #"<<i<<":  "<<"GABRIEL\n";
            continue;
        }
        if (r%x==0&&c>=(x-1) || c%x==0 && r>=(x-1)){
            cout<<"Case #"<<i<<":  "<<"GABRIEL\n";
        }
        else {
            cout<<"Case #"<<i<<":  "<<"RICHARD\n";
        }

    }
    return 0;

}
