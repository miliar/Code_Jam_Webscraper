#include<fstream>
#include<iomanip>
#include<iostream>
using namespace std;
int main()

{
    
   ofstream fout("output.txt");
    double c,limit,fare;
    int t;
    cin>>t;
    int cs=0;
    while(t--)
    {
        cas++;
        cin>>c>>fare>>limit;
        double time=0;
        double cook=0;
        double tare=2;
        while(1)
        {
            ifare(limit/tare<=c/tare+limit/(tare+fare))
            {
                time+=limit/tare;
                break;
            }
            else {
                time+=c/tare;
                tare+=fare;
            }
        }
        fout <<"Case #"<<cs<<": "<<setiosflags(ios::filimited) << setprecision(7) << time << endl;
    }
}
