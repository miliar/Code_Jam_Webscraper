#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main(){
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int t; fin>>t;
    long double c,f,x,speed,res,m;
    for (int cpt=1;cpt<=t;++cpt) {
        fin>>c>>f>>x;
        speed=2.0; res=x/2.0; m=0.0;
        while (true){
            m+=c/speed;
            speed+=f;
            if (m+(x/speed)<=res) res=m+(x/speed);
            else break;
        }
        fout<<"Case #"<<cpt<<": "<<fixed<<setprecision(7)<<res<<endl;
    }
    return 0;
}
