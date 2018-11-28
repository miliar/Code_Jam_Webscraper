#include <iostream>
#include <fstream>
#include <time.h>
#include <cstdlib>
#include <unistd.h>
using namespace std;


int main()
{
    long T,i,j,Smax,a,frnds;
    frnds=0;
    unsigned long long int standCount=0;
    ifstream fi;
    fi.open("A-large.in");
    ofstream myfile;
    myfile.open ("codejam.out");
    fi>>T;
    char c;
    for (i=1;i<=T;i++)          // loop getting single characters
    {

        fi>>Smax;
        fi.get(c);
        standCount=0;
        frnds=0;
        Smax;
        for(j=0;j<=Smax;j++)
        {
            fi.get(c);
            a=(int)c;
            a=a-48;
            if(standCount<j)
            {
                int diff=j-standCount;
                frnds+=diff;
                standCount+=diff;

            }

            standCount+=a;

            //cout << a;

        }
        myfile<<"Case #"<<i<<": "<<frnds<<endl;
    }
    fi.close();
    return 0;

}
