#include<iostream>
#include<iomanip>
#include<cstdlib>
#include<fstream>
using namespace std;
int main(){
    fstream fin,fout;
    fin.open("B-large.in",ios::in);
    fout.open("Bout-large.txt",ios::out);
    int t;
    fin>>t;
    for(int u=0;u<t;u++){
        double c,f,x;
        fin>>c>>f>>x;
        double pro=2,now=0,time=x/2;
        for(;;){
            if(x/pro+now<=time){
                time=x/pro+now;
                now+=c/pro;
                pro+=f;
            }
            else break;
        }
        fout<<"Case #"<<u+1<<": "<<fixed<<setprecision(7)<<time<<endl;
    }
    system("pause");
    return 0;
}
