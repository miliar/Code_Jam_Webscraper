#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;


double calc(double cc,double ff, double xx, double ii, double def)
    {
        double t=0;
        for(double j=1; j<=ii; j++)
        {
            t=t+(cc/def);
            def=def+ff;
            if(j==ii)
            {
                t=t+(xx/def);
            }
        }
        return t;
    }

int main()
{
    double c,f,x,tym,min;
    double n;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>n;

    for(int i=1; i<=n; i++)
    {
        fin>>c;
        fin>>f;
        fin>>x;
        int q=1;
        tym=x/2;
        min=tym;
        double k=1;
        while(q==1)
        {

            tym= calc(c,f,x,k,2);
            if(tym<min)
            {
                min=tym;
                k++;
            }
            else
            {
                q=0;
            }
        }
        fout<<setprecision(7)<<fixed<<"Case #"<<i<<": "<<min<<endl;
    }

    return 0;
}
