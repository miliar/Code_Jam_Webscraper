#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    ifstream infile("B-small-attempt2.in");
    ofstream outfile("B-small-attempt2.txt");

    int t;
    double c,f,x;
    double mintime;
    double tmp;
    int counter;
    infile>>t;
    for(int i=0;i<t;i++){
        infile>>c>>f>>x;
        mintime = 1000000;
        counter = 0;
        tmp = 0;
        while(1){
            tmp = 0;
            for(int j=0;j<counter;j++){
                tmp += c/(2+j*f);
            }
            tmp += x/(2+counter*f);
            if(tmp<mintime){
                mintime = tmp;
                counter++;
            }
            else
                break;
        }
        outfile<<"case #"<<i+1<<": ";
        outfile<<setiosflags(ios::fixed);
        outfile<<setprecision(7)<<mintime<<endl;
    }

    return 0;
}
