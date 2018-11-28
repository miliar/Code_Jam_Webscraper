#include<iostream>
#include<string.h>
#include <fstream>
using namespace std;

int main()
{
    long long int t, k;
    ifstream infile("A-small-attempt3.txt");
    ofstream outfile("A-small-result.out");
    infile>>t;
    k = 1;
    long long int smx;
    long long int i, j, len, StngPrsn, ExtraPrsn;

    while(infile>>smx )
    {
        char Scount[smx + 1];
        infile>>Scount;
        //cout<<smx<<" "<<Scount<<endl;
        len = strlen(Scount);
        StngPrsn = ExtraPrsn = 0;
        //cout<<"len = "<<len<<endl;

        for(i = 0; i < len; ++i)
        {
            if(StngPrsn < i && Scount[i] - 48 != 0)
            {
                //cout<<"in if\n";
                //cout<<"S = "<<StngPrsn<<"    E = "<<ExtraPrsn<<endl;
                ExtraPrsn += i - StngPrsn;
                StngPrsn += ExtraPrsn + Scount[i] - 48;

                //cout<<"S = "<<StngPrsn<<"    E = "<<ExtraPrsn<<endl;
            }
            else
            {
                //cout<<"in else\n";
                //cout<<"S = "<<StngPrsn<<endl;
                StngPrsn += int(Scount[i]) - 48;
                //cout<<"S = "<<StngPrsn<<endl;
            }
        }

        //cout<<"Case #"<<k<<": "<<ExtraPrsn<<endl;
        outfile<<"Case #"<<k<<": "<<ExtraPrsn<<endl;
        ++k;
    }

    return 0;
}
