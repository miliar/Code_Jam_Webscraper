#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    cin>>t;
    for(int i=1; i<=t; i++){
        double c,f,x;
        cin>>c>>f>>x;
        double rate=2.0, time=0;

        while(true){
            if (c/rate+x/(rate+f)<x/rate){
               time+=c/rate;
               rate+=f;
            }
            else {time+=x/rate; break;}
        }
        cout<<showpoint<<setprecision(8)<<"Case #"<<i<<": "<<time<<endl;
    }
    return 0;
}
