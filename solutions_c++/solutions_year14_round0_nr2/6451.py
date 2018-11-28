#include<iostream>
#include<iomanip>
#include<cstdlib>
#include<fstream>
using namespace std;
int main(){
    fstream fin,fout;
    fin.open("B-large.in",ios::in);
    fout.open("Bout-small.txt",ios::out);
    int t;
    fin>>t;
    for(int u=0;u<t;u++){
        double c,f,x;
        fin>>c>>f>>x;
        double produce=2,time_now=0,min_time=x/2;
        for(;;){
            if(x/produce+time_now<=min_time){
                min_time=x/produce+time_now;
                time_now+=c/produce;
                produce+=f;
            }
            else break;
        }
        fout<<"Case #"<<u+1<<": "<<fixed<<setprecision(7)<<min_time<<endl;
    }
    system("pause");
    return 0;
}
