#include <iostream>
#include <fstream>
#include <iomanip>


using namespace std;

int main()
{
    ofstream fout;
    ifstream fin;
    fin.open("B-large.in");
    fout.open ("answers.txt");
    int n;
    fin>>n;
    for(int ctr1=0;ctr1<n;ctr1++)
    {
        double c,f,x;
        fin>>c>>f>>x;
        double factoryPart=0;
        double startingCps=2.0;
        double minimum=x/startingCps;
        double temp;
        while(1)
        {
            factoryPart+=c/startingCps;
            startingCps+=f;
            temp=factoryPart+x/startingCps;
            if(temp<minimum)
            minimum=temp;
            else break;
        }
        fout<<"CASE #"<<ctr1+1<<": "<<fixed<<setprecision(7)<<minimum<<endl;
    }

    fout.close();
    fin.close();
    return 0;
}
