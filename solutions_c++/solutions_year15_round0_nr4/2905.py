#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,x,r,c,i;
    cin>>t;
    for(i=1;i<=t;i++){
        cin>>x>>r>>c;
        if((r*c)%x==0 && r>=x-1 && c>=x-1)
            cout<<"Case #"<<i<<": "<<"GABRIEL"<<"\n";
        else
            cout<<"Case #"<<i<<": "<<"RICHARD"<<"\n";
    }
    return 0;
}


