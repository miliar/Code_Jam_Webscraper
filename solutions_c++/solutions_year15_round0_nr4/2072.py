#include<iostream>

using namespace std;

int main(){
    int T,t=1;
    cin>>T;
    while (t<=T) {
        int X,R,C;
        string ans;
        cin>>X>>R>>C;
        if(X==1){
            ans = "GABRIEL";
        }
        if (X==2) {
            if ((R*C)%2 ==0) {
                ans = "GABRIEL";
            }
            else{
                ans = "RICHARD";
            }
        }
        if(X==3){
            
            ans = "RICHARD";
            if (R%3==0) {
                if ((C%2==0)||(C>2)) {
                    ans = "GABRIEL";
                }
                
            }
            if (C%3==0) {
                if ((R%2==0)||(R>2)) {
                    ans = "GABRIEL";
                }
              
            }

            
        }
        if (X==4) {
            ans = "RICHARD";
            if (R%4==0) {
                if ((C>2)) {
                    ans = "GABRIEL";
                }
                
            }
            if (C%4==0) {
                if ((R>2)) {
                    ans = "GABRIEL";
                }
                
            }
            
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
        t++;
    }
    return 0;
}