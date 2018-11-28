#include <iostream>
using namespace std;
#include<stdio.h>
#include<iomanip>


int main() {
    int i,t;
    freopen("/Users/saintni/Documents/c++/try/try/B-large.in","r",stdin);
   freopen("/Users/saintni/Documents/c++/try/try/output.txt","w",stdout);
    scanf("%d¥n",&i);
   
    for(t=1;t<=i;t++)
    {
        double C,F,X;
        scanf("%lf",&C);scanf("%lf",&F);scanf("%lf",&X);
        
        double speed=2;
        double t_now = X/speed;
        double t_farm = C/speed;
        double t_post = X/(speed+F)+t_farm;

        while(t_post<t_now){
        
            t_now=t_post;
            speed += F;
            t_farm+=C/speed;
            t_post=X/(speed+F)+t_farm;
            
        }
        
        
        cout<<setprecision(15)<<"Case #"<<t<<": "<<t_now<<endl;
    }
    return 0;
}