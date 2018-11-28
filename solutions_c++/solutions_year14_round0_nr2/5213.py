#include<fstream>
#include <string>
#include <sstream>
#include<iomanip>
#include<iostream>
using namespace std;
int main()
{
    ifstream gin("input.txt");
    ofstream gout("output.txt");
    double c,x,f;
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        cas++;
        cin>>c>>f>>x;
        double time=0;
        double cook=0;
        double rate=2;
        while(1)
        {
            if(x/rate<=c/rate+x/(rate+f))
            {
                time+=x/rate;
                break;
            }
            else {
                time+=c/rate;
                rate+=f;
            }
        }
        gout <<"Case #"<<cas<<": "<<setiosflags(ios::fixed) << setprecision(7) << time << endl;
    }
}
