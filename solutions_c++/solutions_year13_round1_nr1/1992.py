#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    long long int i,j,t,p,r,t1,d,sum,co,f,t2;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>t1;
    for(p=1;p<=t1;p++)
    {
        fin>>r>>t2;
        d=2*r-3;
        f=0;
        co=0;
        sum=0;
        while(1)
        {
            f=f+4;
            t=f+d;
            sum=sum+t;
            if(sum<=t2)
            {
                co++;
            }
            else
            break;
        }
        fout<<"Case #"<<p<<": "<<co<<"\n";
    }
    return 0;
}
