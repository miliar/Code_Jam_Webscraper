#include <iostream>
#include <algorithm>
#include <string>
#include <string.h>
#include <math.h>
#include <fstream>
#include <conio.h>
#include <iomanip>
#include <stdio.h>

using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    out.open("output.txt");
    in.open("input.txt");
    int t;
    in>>t;
    for(int v=1;v<=t;v++)
    {

        double c,f,x;
        in>>c>>f>>x;
        double time=0,A=0;
        double i=2;



        while(1)
        {
            if(A>=c)
            {
                if((x-A)/i>((x-A+c)/(i+f)))
                {
                    A-=c;
                    //time+=c/i;
                    i+=f;

                }
                else
                {
                    time+=(x-A)/i;
                    break;
                }
            }
            else
            {
                if(x-A>c)
                {
                    time+=(c-A)/i;
                    A=c;
                }
                else
                {
                    time+=(x-A)/i;
                    break;
                }
            }
        }
        out.setf(ios::fixed,ios::floatfield);
        out.precision(7);
        out<<"Case #"<<v<<": "<<time<<endl;
    }




    return 0;
}
