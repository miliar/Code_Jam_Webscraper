
#include <iostream>
#include <string.h>
#include <vector>
using namespace std;
double check(int NumF, double C, double F, double X);
int main(){
    int NumberOfCases=0;
    double C;
    double F;
    double X; 
    cin>>NumberOfCases;
    cout<<fixed;
    std::cout.precision(7);
    for(int i=0;i<NumberOfCases;i++){
        double num=0;
        cin>>C;
        cin>>F;
        cin>>X;
        while(check(num,C,F,X)>check(num+1,C,F,X)){
                num++;}
    cout<<"Case #"<<i+1<<": "<<check(num, C, F, X)<<endl;
    }  
}
double check(int NumF, double C, double F, double X){
    int TempF=NumF;
    double num=0;
    //cerr<<TempF;
    if(TempF>0){
        num=X/(2+(TempF*F));
    //cerr<<"num: "<<num<<"\t";
    while(TempF>0){
        TempF--;
        num+=C/(2+(TempF*F));
    //cerr<<"num: "<<num<<"\t";
    }
    //cerr<<num;
    return num;}
    return X/2;}


