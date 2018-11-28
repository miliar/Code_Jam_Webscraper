#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <sstream>
#define FOR1(i,n) for(i=1;i<=n;i++)

using namespace std;

int main()
{
    int sm=1;
    char *filin, *filot;
    if(sm)
    {
        filin="A-small-attempt2.in";
        filot="A-small-result.txt";
    }
    else
    {
        filin="A-large.in";
        filot="A-large-result.txt";

    }

ifstream inf;
    ofstream otp;

    inf.open(filin);
    otp.open(filot);

        string line;
    int test, it_test=1;
    getline(inf, line);
    stringstream sline(line);
    sline>>test;
    long double num;
    long ans;


     FOR1(it_test, test)
    {

        getline(inf, line);
        string a="", b="";
        int lim=line.length()-1;
        int i=0;
        while(i<lim)
        {
            if(line[i]==' ')
                break;
            i++;
        }


        a=line.substr(0,i);
        b=line.substr(i+1, lim+1);

           int lena=a.length();
        int lenb=b.length();

        stringstream ssa(a);
        stringstream ssb(b);

        int r,t;
           ssa>>r;
        ssb>>t;

        num=(1-2*r)+ sqrt(4*r*r + 1 - 4*r + 8*t);
        ans=floor(num/4);


//cout<<r<<"----"<<t<<"   "<<ans<<endl;
otp<<"Case #"<<it_test<<": "<<ans<<endl;

        }

    return 0;
}
