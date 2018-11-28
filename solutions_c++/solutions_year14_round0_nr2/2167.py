#include<iostream>
#include<iomanip>
using namespace std;
int k,t;
double cps;
double tim;
double solve(){
    tim=1.0;cps=2.0;
    double cost,farm,x;
    cin>>cost>>farm>>x;
    while(1){
        if(tim+x/cps>tim+cost/cps+x/(cps+farm)){
            tim+=cost/cps;
            cps+=farm;
        }
        else{
            tim=tim+x/cps;
            return tim-1.0;
        }
    }
}
int main()
{
    cin>>k;
    for(t =1; t <=k; t ++){
    cout<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<solve()<<endl;
    }
    return 0;
}