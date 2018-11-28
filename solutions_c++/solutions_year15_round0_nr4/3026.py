#include<bits/stdc++.h>
using namespace std;
//This works for only D-SMALL
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        int x,r,c;
        cin>>x>>r>>c;
        int tot = r*c;
        if(x==1){
            cout<<"Case #"<<i<<": GABRIEL"<<endl;
        } else if( x==2 ) {
            if( tot%2 ){
                cout<<"Case #"<<i<<": RICHARD"<<endl;
            } else {
                cout<<"Case #"<<i<<": GABRIEL"<<endl;
            }
        } else if( x==3 ) {
            if( (tot%3==0) and (r>=2 and c>=2)){
                cout<<"Case #"<<i<<": GABRIEL"<<endl;
            } else {
                cout<<"Case #"<<i<<": RICHARD"<<endl;
            }
        } else if( x==4 ) {
            if( (tot%4==0) and r>2 and c>2 ){
                cout<<"Case #"<<i<<": GABRIEL"<<endl;
            } else {
                cout<<"Case #"<<i<<": RICHARD"<<endl;
            }
        } else {
            cout<<"Sorry this can't handle big test data"<<endl;
        }
    }
    return 0;
}