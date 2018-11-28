//#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
ifstream cin("B-large.in");
ofstream cout("B-large.out");
int main()
{
    int zz;
    cin>>zz;
    for(int ii=0;ii<zz;ii++)
    {
        double c,f,x,t=0,u=2;
        cin>>c>>f>>x;
        while(x/u>(c/u)+(x/(u+f)))
        {
            t+=(c/u);
            u+=f;
        }
        t+=x/u;
        cout<<"Case #"<<ii+1<<": "<<fixed<<setprecision(7)<<t<<endl;
    }
    //system("pause");
}
