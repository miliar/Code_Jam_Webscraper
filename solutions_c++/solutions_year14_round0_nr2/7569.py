#include <iostream>
#include<fstream>
#include<iomanip>

using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large-output0.out");

    //ifstream fin("test.in");
    //ofstream fout("test.out");

    int t, i,j,k,l;
    double c, f, x;
    double temp=0,mx=0,prev, inc=2;
    fin>>t;
    for(l=0;l<t;l++)
    {
        fin>>c;
        fin>>f;
        fin>>x;
        temp=0;
        mx=0;
        prev = x/2;
        inc=2;
        //cout<<setprecision(7)<<fixed;
        //cout<<c<<" "<<f<<" "<<x<<"\n";

        while(1)
        {
            temp+=c/inc;
            mx = temp+ x/(inc+f);
            if(mx<prev)
            {
                prev = mx;
                inc = inc+f;
            }
            else
                break;
        }

            fout<<setprecision(7)<<fixed;
            fout<<"Case #"<<l+1<<": "<<prev<<"\n";



    }

    return(0);

}


