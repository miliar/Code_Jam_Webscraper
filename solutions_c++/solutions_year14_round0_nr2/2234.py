#include<string>
#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int i, T;
    double C, F, X, gaint, total, spendTime;
    cin>>T; 
   
    for(i = 0; i < T; i++){
        spendTime = 0;
        gaint = 2.0;
        total = 0.0;
        cin>>C>>F>>X;
        while(true){
            // cout<<spendTime<<endl;
            if(X / gaint >= X / (gaint + F ) + C / gaint) {
                // total -= C;
                spendTime += C / gaint  ;
                gaint += F;
                
            }else{
                spendTime += X / gaint;
                break;                
            }
            // break;
             // cout<<spendTime<<endl;
        }

        cout<<"Case #"<<i+1<<": ";
        printf("%.7f\n", spendTime);
        // cout<<endl;
    }
    return 0;
}
