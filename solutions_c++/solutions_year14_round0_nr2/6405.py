#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
    ifstream infile;
    ofstream outfile;
    infile.open("B-large.in");
    outfile.open("B-large.out");
    int t , n , i , j;
    double c , f , x , time , s , newtime;
    while(infile >> t)
    {
        for(i = 0 ; i < t ; i++)
        {
            infile >> c >> f >> x;
            s = 2.;
            time = x / s;
            newtime = 0.;
            while(time > newtime + c / s + x / (s + f))
            {
                time = newtime + c / s + x / (s + f);
                newtime = newtime + c / s;
                s = s + f;
            }
            outfile << "Case #" << i+1 << ": " << setiosflags(ios::fixed)
        <<setprecision(7) <<time << endl;
        }
    }
    infile.close();
    outfile.close();
    return 0;
}
