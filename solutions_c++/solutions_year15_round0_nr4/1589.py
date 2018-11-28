#include <iostream>
using namespace std;

int main() {
   
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    
    int x,r,c;
    int t;
    cin>>t;
    for(int ti=1;ti<=t;ti++){
        cin>>x>>r>>c;
        if(x==1){
            cout<<"Case #"<<ti<<":"<<" GABRIEL"<<endl;
            continue;
        }
        if(x==2){
            if((r*c)%2)
                cout<<"Case #"<<ti<<":"<<" RICHARD"<<endl;
            else
                cout<<"Case #"<<ti<<":"<<" GABRIEL"<<endl;
            continue;
        }
        if(x==3){
            if((r*c)%3)
            {
                cout<<"Case #"<<ti<<":"<<" RICHARD"<<endl;
                continue;
            }
            if(r*c>3)
            {
                cout<<"Case #"<<ti<<":"<<" GABRIEL"<<endl;
                continue;
            }
            cout<<"Case #"<<ti<<":"<<" RICHARD"<<endl;
            continue;
        }
        if(x==4){
            if((r*c)>=12)
            {
                cout<<"Case #"<<ti<<":"<<" GABRIEL"<<endl;
                continue;
            }
            cout<<"Case #"<<ti<<":"<<" RICHARD"<<endl;
            continue;
        }
        else{
            cout<<"Case #"<<ti<<":"<<" RICHARD"<<endl;
        }
        
        
    }
    return 0;
}