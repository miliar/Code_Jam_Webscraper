#include<iostream>
#include<fstream>
#include<stdlib.h>

using namespace std;

int main()
{
    ifstream ifs;
    ofstream ofs;
    ifs.open("A-small-attempt0.in");
    ofs.open("Out.txt");
    int test, smax;
    char *str;
    ifs>>test;
    for(int k = 0; k<test; k++)
    {
        ifs>>smax;
        int total = 0;
        str = new char[smax+2];
        ifs>>str;
        if(smax==0)
        {
            ofs<<"Case #"<<k+1<<": "<<0<<endl;
            continue;
        }
        char b[2];
        b[1]='\0';
        b[0]=str[0];
        int nops = atoi(b), req = 0, dig;
        for(int i=1; i<=smax; i++)
        {
            b[0]=str[i]; dig=atoi(b);
            if(dig==0)
                continue;
            else
            {
                int dif = i-nops;
                if(dif>0)
                {
                    req = req+dif;
                    nops+=req;
                    nops+=dig;
                }
                else
                    nops+=dig;
            }
        }
        ofs<<"Case #"<<k+1<<": "<<req<<endl;
    }
    ifs.close();
    ofs.close();
    return 0;
}
