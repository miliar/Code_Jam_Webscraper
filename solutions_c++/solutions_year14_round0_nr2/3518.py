#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;
int main(){
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    int cases;
    double c, f, x, time;
    in>>cases;
    int i =0;
    double speed = 2;
    while(i<cases){
        time =0;
        speed = 2;
        in>>c;
        in>>f;
        in>>x;
        while((c/speed)+(x/(speed+f)) < x/speed){
            time += c/speed;
            speed += f;
        }
        
        //cout<<c<<"  "<<f<<"  "<<x<<"  "<<endl;
        time =time + x/speed;
        //printf("Case #%d: %.7f\n", i+1, time);
        out<<fixed<<setprecision(7);
        out<<"Case #"<<i+1<<": "<<time<<endl;
        i++;   
    }
    //system("pause");
    return 0;   
}
