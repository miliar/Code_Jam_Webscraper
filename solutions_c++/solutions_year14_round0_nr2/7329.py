#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
using namespace std;
ifstream in("in.in");
ofstream out("out.out");
int main(){
    out<<setprecision(7);
    out<<fixed;
    int t,l;
    in>>t;
    l=1;
    while(t>0){
        double speed=2;
        double time=0;
        double c,f,x;
        in>>c>>f>>x;
        while((x/speed)>(c/speed)+(x/(speed+f))){
           time+=c/speed;
           speed+=f;
        }
        time +=x/speed;
        out<<"Case #"<<l<<": "<<time<<endl;
        t--;
        l++;
    }
    return 0;
}
