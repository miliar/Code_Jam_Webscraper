#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    int n;
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("output.txt");
    fin>>n;
    for(int k=1;k<=n;++k)
    {
        double c,f,x;
        fin>>c>>f>>x;
        fout<<"Case #"<<k<<": ";
        double ans=0,p=2,t=0;
        /*if(x<=c)
        {
            fout<<x/2<<endl;
            continue;
        }*/
        while(1)
        {
            if(x/p<c/p+x/(p+f))
            {
                fout<<fixed<<setprecision(7)<<t+x/p<<endl;
                break;
            }
            t+=c/p,p+=f;
        }
    }
    return 0;
}
