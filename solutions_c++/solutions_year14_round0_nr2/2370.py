#include<iostream>
#include<fstream>
#include<iomanip>
#include<stdlib.h>

using namespace std;

int main()
{
    char ds[50];
    int T,d=1;
    long double c,f,x,temp1,temp2,tf,tt;
    ifstream f1;
	f1.open("F:\\TC\\BIN\\Code_Jam_2\\IS2.in");
	ofstream f2;
	f2.open("F:\\TC\\BIN\\Code_Jam_2\\OS2.out");
    f1>>T;
    
    while(T>0)
    {
    tf=2.0;
    tt=0.0;
    f1.getline(ds,50,' ');
    c=atof(ds);
    f1.getline(ds,50,' ');
    f=atof(ds);
    f1.getline(ds,50,'\n');
    x=atof(ds);
    if(x<=c)
        tt+=(x/tf);
    else
    {
        temp1=x/tf;
        temp2=tt+(c/tf)+(x/(tf+f));
        while(temp2<(temp1+tt))
        {
            tt+=(c/tf);
            tf+=f;
            temp1=x/tf;
            temp2=tt+(c/tf)+(x/(tf+f));
        }
        tt+=temp1;
    }
    if(d!=1)
        f2<<"\n";
    f2<<"Case #"<<d<<": "<<setprecision(15)<<tt;
    T--;
    d++;
    }
    f1.close();
    f2.close();
    return 0;	
}
