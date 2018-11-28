#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iomanip>
#include<fstream>
using namespace std;
int main()
{
    fstream fin,fout;
//    fin.open("B-small-attempt0.in",ios::in);
//    fout.open("B-small-attempt0.out",ios::out);
    fin.open("B-large.in",ios::in);
    fout.open("B-large.out",ios::out);
    int T;
    fin>>T;
    double c,f,x;
    for(int i=1;i<=T;++i)
    {
        fin>>c>>f>>x;
        double speed=2,time=0;
        while((x-c)*(speed+f)>x*speed)
        {
            time+=c/speed;
            speed+=f;
        }
//        cout<<"Case #"<<i<<": "<<setprecision(7)<<setiosflags(ios::fixed)<<time+x/speed<<endl;
        fout<<"Case #"<<i<<": "<<setprecision(7)<<setiosflags(ios::fixed)<<time+x/speed<<endl;
    }
    return 0;
}
