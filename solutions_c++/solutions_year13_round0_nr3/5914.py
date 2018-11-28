#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
#include <stdlib.h>

#include <sstream>
using namespace std;
bool palindrom(long k)
{
    char *num;
    stringstream ss;
    ss << k;
    string str = ss.str();
    string number=str;
    bool jo=true;
    long i=0;

    while ((i<number.length()/2)&&jo)
    {
        jo=number[i]==number[number.length()-i-1];
        i++;
    }
    return jo;
}
int main()
{
   // cout<< palindrom(10)<<"\n"<< palindrom(121)<<"\n"<<palindrom(3);
    ifstream f("C-small-attempt0.in");
    ofstream fki;
    fki.open("fair.out");
    long int t,a,b,ossz;
    f >> t;
    for (int i=1; i<=t; i++)
    {
    ossz=0;
    f>> a>>b;
    for (long int k=int(sqrt(a-1))+1;k<=sqrt(b); k++)
    {
        if (palindrom(k) and (palindrom(k*k))){ossz++;}
    }
    fki<< "Case #"<< i<<": "<< ossz<< "\n";
    }
    fki.close();
    f.close();
}


