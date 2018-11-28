#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int n;
    fin>>n;
    double C,F,X;
    double time=0,remaining,rate;
    for(int i=1;i<=n;i++)
    {
        fin>>C>>F>>X;
        rate=2;
        time=0;
        remaining=X;
        while(1)
        {
            if((X/rate)>((C/rate)+(X/(rate+F))))
            {
                time+=C/rate;
                rate+=F;
            }
            else
            {
                time+=X/rate;
                fout<<"Case #"<<i<<": "<<setprecision(7)<<fixed<<time<<endl;
                break;
            }
        }
    }

    return 0;
}
