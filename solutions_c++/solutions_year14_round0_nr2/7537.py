#include<cstdio>
#include<iomanip>
#include<fstream>
using namespace std;
int T;
double C,F,X,N,Time;
int main(){
    ifstream fin;
    fin.open("B-large.in");
    ofstream fout;
    fout.open("outputBL.txt");
    fin>>T;
    for(int i=1;i<=T;++i){
        double curTime=0.0;
        double nextTime=0.0;
        N=2.0;
        Time=0.0;
        fin>>C>>F>>X;
        curTime = X/N+Time;
        Time = C/N+Time;
        N+=F;
        nextTime = Time+X/N;
        while(curTime>nextTime){
            curTime = X/N+Time;
            Time = C/N+Time;
            N+=F;
            nextTime = Time+X/N;
        }
        fout<<"Case #"<<i<<": "<<std::fixed << std::setprecision(10) <<curTime<<endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
