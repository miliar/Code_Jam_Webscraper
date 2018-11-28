#include<fstream>
#include<iostream>
#include<iomanip>
using namespace std;
std::ifstream input("B-large.in");
std::ofstream output("output.out");
int T;
long double C,F,X;
int main(){
    input>>T;
    for(int i=1;i<=T;i++){
           input>>C>>F>>X;
           bool flag=1;long double t1,tc,t2,tt,V,V2;
           tt=0;V=2;
           while(flag){
               t1=X/V;
               tc=C/V;
               V2=V+F;
               t2=X/V2;
               if(t1<t2+tc){
                    tt+=t1;
                    output<<"Case #"<<i<<": "<<std::setprecision(10)<<tt<<"\n";
                    flag=0;
                       }
               else {
                    V=V2;
                    tt=tt+tc;
                    } 
           }                
    }
    return 0;
}
