#include<iostream>
#include<iomanip>

using namespace std;

int main(){
    int o;
    cin>>o;
    for(int cases=0; cases<o; cases++){
        long double c,f,x;
        cin>>c>>f>>x;
        long double mintime=100000000, tempmin=x/2;
        long double time=0;
        long double rate=2;
        do{
            if (tempmin<mintime){mintime=tempmin;}
            time+=c/rate;
            rate+=f;
            tempmin=time+(x/rate);
        }while(mintime>=tempmin);
        cout<<fixed<<setprecision(7);
        cout<<"Case #"<<cases+1<<": "<<mintime<<endl;
    }
    return 0;
}
