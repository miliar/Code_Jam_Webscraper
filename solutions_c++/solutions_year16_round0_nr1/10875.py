#include <iostream>
#include <stdio.h>
using namespace std;
int counted[10]={0,0,0,0,0,0,0,0,0,0};
bool check(int nu){
    while(nu>=1){
        counted[nu%10]=1;
        nu/=10;
    }
    if(counted[0] == 1 && counted[1] == 1 && counted[2] == 1 && counted[3] == 1 && counted[4] == 1 && counted[5] == 1 && counted[6] == 1 && counted[7] == 1 && counted[8] == 1 && counted[9] == 1){
        return true;
    }else{
        return false;
    }
}
int main(void) {
    int i=0;
    int nu=0;
    int nus=0;
    cin>>i;
    for(int q=1;q<=i;q++){
        cin>>nu;
        nus = nu;
        cout<<"Case #"<<q<<": ";
        if(nu == 0){
            cout<<"INSOMNIA"<<endl;
        }else{
            for(int j=1; j>-1; j++){
                if(check(nus)){
                    cout<<nus<<endl;
                    break;
                }else{
                    nus = nu*(j+1);
                }
            }
            counted[0]=0;
            counted[1]=0;
            counted[2]=0;
            counted[3]=0;
            counted[4]=0;
            counted[5]=0;
            counted[6]=0;
            counted[7]=0;
            counted[8]=0;
            counted[9]=0;
        }
    }
}