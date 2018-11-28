#include<iostream>
using namespace std;
int main(){
    int t,p=0;
    cin>>t;
    while(t--){
        p++;
        int x,r,c;
        cin>>x>>r>>c;
        int l=(r*c);
        int k=min(r,c);
        bool ans=0;
        switch(x){
            case 1: ans=1;
                    break;
            case 2: if(l%2==0){
                        ans=1;
                    }
                    break;
            case 3:if(k>=2&&l%3==0){
                        ans=1;
                    }
                    break;
            case 4:if(k>=3&&l%4==0){
                        ans=1;
                    }
                    break;
            case 5:if(k>=4&&l%5==0){
                        ans=1;
                    }
                    break;
            case 6:if(k>=4&&l%6==0){
                        ans=1;
                    }
            case 7:break;

        }
        if(ans){
            cout<<"Case #"<<p<<": GABRIEL\n";
        }else{
            cout<<"Case #"<<p<<": RICHARD\n";
        }
    }
}

