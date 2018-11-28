#include <iostream>
#include <stdio.h>
#include <fstream>
#define oo 1e9
using namespace std;
double C,F,X;
double min(double a,double b){
    if(a<b)
        return a;
    return b;
}
double selled(int nbrTimes){
    double time=0;
    double r=2;
    for(int i=0;i<nbrTimes;i++){
        time+=(C/r);
        r+=F;
    }
    return time+X/r;
}
double solve(double ratio){
    if(ratio>X)
        return 0;
    //cout<<ratio<<endl;
    return min(X/ratio,C/ratio+solve(ratio+F));
}

int main()
{
    ifstream cin("input.txt");
    FILE* f;
    f=fopen("output.txt","w");
    int t;
    int c=0;
    cin>>t;
    while(t--){
            c++;
    cin>>C>>F>>X;
        double sol=selled(0);
        int nbrTimes=0;
        while(true){
            nbrTimes++;
            double nsol=selled(nbrTimes);
            if(sol>nsol)
                sol=nsol;
            else
                break;
        }
        //cout<<sol<<endl;
    fprintf(f,"Case #%d: %0.7f\n",c,sol);
    //cout<<s<<endl;
    }
    fclose(f);

}
