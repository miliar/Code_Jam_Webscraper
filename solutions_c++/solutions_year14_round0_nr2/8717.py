#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<iomanip>
using namespace std;
int main()
{
    fstream myfile("B-large.in");
    fstream out("out.txt");

    if(myfile.is_open())
    {
        int t;
        myfile>>t;

        for(int test=1;test<=t;test++)
        {

            double C,F,X,ans=0;
            myfile>>C>>F>>X;

            double iRate=2;

            bool finish=false;
            while(!finish)
            {
                double fut= C/iRate +X/(iRate+F);
                double cStop=X/iRate;
                if(fut<cStop) {ans+=C/iRate; iRate+=F; }
                else {finish=true; ans+=X/iRate;}
            }
            out<<"Case #"<< setprecision(15)<<test<<": "<<ans<<"\n";

        }
    }
    myfile.close(); out.close();


    return 0;
}
