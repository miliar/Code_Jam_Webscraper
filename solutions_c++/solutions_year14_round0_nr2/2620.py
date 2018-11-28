#include<iostream>
#include<stdio.h>
#include<string.h>
#include<iomanip>

using namespace std;

int main(){

    int T;
    double C, F, X, sum, incrementer, cookie;

    cin>>T;

    for(int i=0; i<T; i++){

        cin>>C>>F>>X;
        sum=0;
        incrementer=2;
        while(1){
            if((sum+(C/incrementer)+(X/(incrementer+F)))<(sum+(X/incrementer))){
                sum=sum+(C/incrementer);
                incrementer = incrementer+F;
            }
            else{
                sum=sum+(X/incrementer);
                break;
            }
        }
        cout<<std::fixed<<std::setprecision(7)<<"Case #"<<i+1<<": "<<sum<<endl;

    }

    return 0;
}
