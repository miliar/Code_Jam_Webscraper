#include <iostream>
#include<iomanip>
using namespace std;

int main()
{
        int Tc;
        cin>>Tc;
        double c[Tc],f[Tc],x[Tc],sol[Tc];
        double done,rate;
        for(int t=0;t<Tc;t++){
            cin>>c[t];
            cin>>f[t];
            cin>>x[t];
        }
        for(int t=0;t<Tc;t++){
                sol[t]=0;
                rate=2;
                done=0;
                while(true){
                    if(x[t]-done>c[t]){
                        sol[t]+=c[t]/rate;
                        done+=c[t];
                        if((x[t]-done)/rate>(x[t]-done+c[t])/(rate+f[t])){
                            done-=c[t];
                            rate+=f[t];
                        }
                    } else {
                        sol[t]+=(x[t]-done)/rate;
                        cout<<"Case #"<<t+1<<": "<<setprecision(7)<< setiosflags(ios::fixed)<< setiosflags(ios::showpoint)<<sol[t]<<endl;
                        done=x[t];
                        break;
                    }
                }
        }
}
