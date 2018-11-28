#include <iostream>
#include <iomanip>

using namespace std;
int main(){
    double C,F,X,R=2.0,cookie=0.0;
    double t1=0.0,t2=0.0,tmp=0.0;
    int flag=0,i,test;
    cin>>test;
    for(i=1;i<=test;i++){
        cookie=0,t1=0.0,t2=0.0;
        flag=0;
        R=2.0;
        cin>>C>>F>>X;
        while(flag!=1){
            t1=X/R+cookie;
            tmp=C/R;
            t2=X/(R+F)+tmp+cookie;
            if(t1<t2){
                flag=1;
                cout<<"Case #"<<i<<": "<<std::fixed<<std::setprecision(7)<<t1<<endl;
            }
            cookie=C/R+cookie;
            R=R+F;
        }
    }
    return 0;
}
