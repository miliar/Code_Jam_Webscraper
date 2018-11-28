
#include <iostream>
#include <fstream>
#include<iomanip>
//#include <string>

using namespace std;

int main() {
    ofstream fout ("test.out");
    ifstream fin ("test.in");
    int tes;
    fin>>tes;
    for(int a=1;a<=tes;a++)
    {
                           
                           double reqd,rate,total,time,min=100000;
                           int i=0;
                           fin>>reqd>>rate>>total;
                           
                           do
                           {
                               int j=i;                   
                               time=0;
                               time+=total/(2+rate*j);
                               j--;
                               while(j>=0)
                               {
                                       time+=reqd/(2+rate*j);
                                       j--;
                               }
                               if(time<min)
                               {
                                           min=time;
                               }
                               i++;
                           }
                           while(time<=min);
                                     
                           fout.setf(ios::fixed);
                                     
                           fout<<"Case #"<<a<<": "<<setprecision(7)<<min<<endl;
    }
    return 0;
}
