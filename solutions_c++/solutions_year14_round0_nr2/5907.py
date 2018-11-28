#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
ifstream fin("C:\\Users\\yanta_000\\Downloads\\B-large.in");
ofstream fout("out.out");
int main()
{
    int test_num;
    double C,F,X;
    double current,time;
    fin>>test_num;
    for(int i=1;i<=test_num;++i){
        time=0.0;
        current=2.0;
        fin>>C>>F>>X;
        double limit=X*F/C-F;
        while(current<limit){
            time+=C/current;
            current+=F;
        }
        time+=X/current;
        fout<<"Case #"<<i<<": "<<setprecision(9)<<time<<endl;
    }
    return 0;
}
