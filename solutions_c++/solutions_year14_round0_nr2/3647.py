#include <iostream>
#include <string>
#include <string.h>
#include <fstream>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int main()
{
    ifstream input;
    input.open("large.txt");
    ofstream output;
    output.open("largeo.txt");
    int t;
    input>>t;

    for(int cse=1;cse<=t;cse++)
    {
        long double time=0;
        long double c,f,x;
        input>>c>>f>>x;

        long double farms=(x/c)-(2/f)-1;

        int n= (int) farms;
        if((x-c)/(2+n*f)>x/(2+f+n*f))
        {
            n++;
        }
        cout<<cse<<"n="<<n<<endl;
        if(n<=0)
        {
            time=x/2;
        }
        else
        {
            int i;
            for (i=0;i<n;i++)
            {
                time+=c/(2+i*f);

            }
            cout<<x/(2+i*f)<<endl;
            time+=x/(2+i*f);

        }

        output<<"Case #"<<cse<<": "<<setprecision(20)<<time<<endl;





    }

    return 0;

}
