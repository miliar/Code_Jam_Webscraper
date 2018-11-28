#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    int t;
    double C, F, X;
    cin>>t;
    for(int n=1;n<=t;n++){
        double R=2;
        cin>>C>>F>>X;
        double t1=X/R, t2=0;
        double buyingTime = C/R;
        double newRate = F+R;
        t2= buyingTime + X/newRate;
        while(t1>t2){
            t1=t2;
            buyingTime += C/newRate;
            newRate = newRate + F;
            t2= buyingTime + X/newRate;
        }
        cout<<"Case #"<<n<<": ";
        printf("%.7f\n",t1);
    }
    return 0;
}
