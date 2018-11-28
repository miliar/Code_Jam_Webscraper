#include<iostream>
#include <iomanip>
using namespace std;

#define local
#ifdef local
#include<fstream>
ifstream fin("B-large.in");
ofstream fout("data.out");
#define cin fin
#define cout fout
#endif // local

int main()
{
    int t,i,j,k;
    double c,f,x;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        double time=0,p=2;
        cin>>c>>f>>x;
        while((f+p)*c<x*f)
        {
            time+=c/p;
            p+=f;
        }
        time+=x/p;
        cout<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<time<<endl;
    }
    return 0;
}
