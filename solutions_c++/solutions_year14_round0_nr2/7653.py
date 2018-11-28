#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int n;
    double oldFarm=2,newFarm;
    double farmIncreaseSize=0,Cost,X;
    double min=0,time, buyNewFarmTime;
    int i=0;
    cin>>n;
    while(i++<n){
       cin>>Cost>>farmIncreaseSize>>X;
        oldFarm=2;
        min=X/oldFarm;
        buyNewFarmTime=0; 
        while(1){
            buyNewFarmTime+=Cost/oldFarm;
            newFarm=oldFarm+farmIncreaseSize;
            time=buyNewFarmTime+X/newFarm;
            oldFarm=newFarm;
            if(time>=min)
                break;
            else
                min=time;
        }

            cout<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<min<<endl;
    }
    return 0;
}
