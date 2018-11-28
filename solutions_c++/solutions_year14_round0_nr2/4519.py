#include<iostream>
using namespace std;


int T;
double C,F,X;


int main(){
    freopen("B-large.in","r",stdin);
    freopen("largeoutput.txt","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;++cas){
        cin>>C>>F>>X;
        double CT = 0;
        double CV = 2;
        double res = 1e100;
        for(int i=0;i<2000000;++i){
            res<?=(X/CV+CT);
            CT = CT+C/CV;
            CV+=F;
        }
        printf("Case #%d: %0.7lf\n",cas,res);
        
    }
    return 0;
}
