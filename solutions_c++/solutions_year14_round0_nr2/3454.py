#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstdlib>
#include<cmath>
using namespace std;
void calcTime(double r,double c,double f,double x,int n)
{
    double time=0;
    double minT,minTT;
    minT=x/r;
    minTT=(c/r)+(x/(f+r));
    while(minTT<=minT)
    {
        time+=c/r;
        r+=f;
        minT=x/r;
        minTT=(c/r)+(x/(f+r));
    }
    time+=x/r;
    fstream fout;
    fout.open("out.txt",ios::out|ios::app);
    fout.unsetf ( std::ios::floatfield );
    fout.setf( std::ios::fixed );
    fout.precision(7);
    fout<<"Case #"<<(n-1)<<": "<<time<<endl;
    fout.close();
}
int main()
{
    double r=2,c,f,x;
    int n;
    fstream fin;
    fin.open("B-large.in",ios::in);
    fin>>n;
    int i=1;
    while(i++<(n+1))
    {
        fin>>c>>f>>x;
        calcTime(r,c,f,x,i);
    }
    fin.close();

}
