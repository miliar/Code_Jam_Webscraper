#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    int cs = 1;
    while(t--){


        cout<<"Case #"<<cs++<<": ";
        int n,r,c;
        cin>>n>>r>>c;
        if(n==1){
            cout<<"GABRIEL"<<endl;
            continue;
        }

        if(n==2){
            if(r%2==0 || c%2==0)cout<<"GABRIEL"<<endl;
            else cout<<"RICHARD"<<endl;
            continue;
        }

        if(n==3){
            if( r*c % 3 == 0 && (r>=2 && c>=2))cout<<"GABRIEL"<<endl;
            else cout<<"RICHARD"<<endl;
            continue;
        }

        if( (r>=3 && c>=3) && (r*c % 4 == 0)){
            cout<<"GABRIEL"<<endl;
            continue;
        }
        cout<<"RICHARD"<<endl;
        continue;
    }
}
