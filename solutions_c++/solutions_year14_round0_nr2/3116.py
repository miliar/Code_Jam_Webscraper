#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("B-large.in");
    ofstream fout;
    fout.open("B-large.out");
    int t;
    double c, f, x, min=0, cost;
    fin>>t;
    fout<<fixed;
    for(int k=1;k<=t;k++)
    {
            fin>>c>>f>>x;
            min=x/2;
            for(double i=1;i<x/c;i++)
            {
                      cost = 0;
                      for(double j=1;j<=i;j++)
                                cost+=c/(2+(j-1)*f);
                      cost+=x/(2+i*f);
                      if(cost<min)
                                  min = cost;
            }
            fout<<"Case #"<<k<<": "<<setprecision(7)<<min<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
