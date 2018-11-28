#include<iostream>
#include<vector>
using namespace std;

int main(){
    int t;
    cin>>t;
    for(int test=1; test <=t; test++){
        double C, F, X;
        cin>>C>>F>>X;
        double prev_f = 2.0;
        double next_f = prev_f + F;
        double time = 0.0;
        while(true){
            if( X * next_f < C * next_f + X * prev_f){
                time += X / prev_f;
                break;
            }
            else{
                time += C / prev_f;
                prev_f = next_f;
                next_f = prev_f + F;
            }
        }
        printf("Case #%d: %.7f\n",test, time);
    }

}
