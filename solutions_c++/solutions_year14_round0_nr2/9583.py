#include<iostream>
#include<iomanip>
#include<algorithm>
#include<cstdio>
using namespace std;
double C,F,X;
double func(double r,double time){//,int n){//current cookies//rate of cookies
    //cout<<"r="<<r<<" time="<<time<<endl;//cin.get();
    //if(cc>=X){cout<<"cc>=X"<<endl;return time;}
    //cout<<"X/r="<<X/r<<" (X/(r+F)+(C/r))="<<(X/(r+F)+(C/r))<<endl;
    //if(n>1000)return time+(X/r);
    if(X/r<= (X/(r+F)+(C/r)) ){
            //cout<<"other basecase"<<endl;
            return time+(X/r);}
    double t=func(r+F,time+(C/r));
    //cout<<"comparing between t="<<t<<" and X/r="<<X/r<<endl;
    return min(t,time+(X/r));
}
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int howmany;
    cin>>howmany;
    for(int count=1;count<=howmany;count++){
        cin>>C>>F>>X;
        cout<<"Case #"<<count<<": ";
        cout  << fixed<<setprecision(7) <<func(2,0)<<endl;
    }
    return 0;
}
