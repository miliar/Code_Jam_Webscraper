//Small Input: ACCEPTED!!!
//Large Input: Pending ???
#include<iostream>
#include<iomanip>
#include<stdio.h>
using namespace std;

int main(){

int T;
double C,F,X;

//freopen("G:\\ACM\\CodeJam2014\\B-large.in","r",stdin);
//freopen("G:\\ACM\\CodeJam2014\\cook_out.txt","w",stdout);
cin>>T;

for(int t=1; t<=T; t++){

    cin>>C>>F>>X;

    cout<<"Case #"<<t<<": ";
    double min_val = X/2;

    //if(C>=X||X<=2) {
    if(X==2) {
            min_val = 1;
            printf("%0.7lf", min_val);
            cout<<endl;
            continue;
    }

    if(C>=X||X<=2) {
            min_val = X/2;
            printf("%0.7lf", min_val);
            cout<<endl;
            continue;
    }

    double div=2;

    double tot=0;

    while(1){
        tot = tot + C/div;
        div = div + F;
        if( tot + (X/div) <= min_val ) min_val = tot + (X/div);
        else break;
    }

    printf("%0.7lf", min_val);
    cout<<endl;
}

}
