#include <iostream>
#include <fstream>
using namespace std;


int main()
{
    int testCases;

    ifstream file("in.txt",ios::in);
    ofstream out("out.txt",ios::out);
    file>>testCases;
    double C, X, F;
    for (int nCase=0; nCase<testCases; nCase++)
    {
        file>>C>>F>>X;

        bool done=false;
        double totalTime = 0;
        double currentRate = 2.0;
        while (!done)
        {
            if ( (C/currentRate+X/(currentRate+F))> (X/currentRate) )
            {
                done=true;
                totalTime+=X/currentRate;
            }
            else{
                totalTime+=C/currentRate;
                currentRate += F;
            }

        }
        out.precision(10);
        out << "Case #"<<nCase+1<<": "<<totalTime<<endl;

    }
    file.close();
    out.close();
    cout << "Done!" << endl;
    return 0;
}
