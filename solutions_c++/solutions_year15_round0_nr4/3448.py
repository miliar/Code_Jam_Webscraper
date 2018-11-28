#include <iostream>
using namespace std;

int main() {
   
   
    int t;
    int x,r,c;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>x>>r>>c;
        if(x==1){
            cout<<"Case #"<<i<<":"<<" GABRIEL"<<endl;
            continue;
        }
        if(x==2){
            if((r*c)%2)
                cout<<"Case #"<<i<<":"<<" RICHARD"<<endl;
            else
                cout<<"Case #"<<i<<":"<<" GABRIEL"<<endl;
            continue;
        }
        if(x==3){
            if((r*c)%3)
            {
                cout<<"Case #"<<i<<":"<<" RICHARD"<<endl;
                continue;
            }
            if(r*c>3)
            {
                cout<<"Case #"<<i<<":"<<" GABRIEL"<<endl;
                continue;
            }
            cout<<"Case #"<<i<<":"<<" RICHARD"<<endl;
            continue;
        }
        if(x==4){
            if((r*c)>=12)
            {
                cout<<"Case #"<<i<<":"<<" GABRIEL"<<endl;
                continue;
            }
            cout<<"Case #"<<i<<":"<<" RICHARD"<<endl;
            continue;
        }
        else{
            cout<<"Case #"<<i<<":"<<" RICHARD"<<endl;
        }
        
        
    }
    return 0;
}
