#include<iostream>
#include<stdio.h>
#include<fstream>
#include<iomanip>
using namespace std;
int main(){
    ifstream in;
    in.open("input.txt");
    ofstream op;
    op.open("output.txt");
    int t,l;
    in>>t;
    for(l=1;l<=t;l++){
        double c,f,x,p,ans,temp;
        in>>c>>f>>x;
        op<<fixed;
        op<<"Case #"<<l<<": ";
        if(x<=c)
            op<<setprecision(7)<<x/2.0<<endl;
        else{
            ans=0.0;
            p=2.0;
            while(1){
                ans+=c/p;
                temp=(x-c)/p;
                p+=f;
                if(x/p>=temp){
                    ans+=temp;
                    break;
                }
            }
            op<<setprecision(7)<<ans<<endl;
        }
    }
    return 0;
}
