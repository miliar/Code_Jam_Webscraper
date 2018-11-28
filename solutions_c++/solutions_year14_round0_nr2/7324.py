#include <iostream>
#include <iomanip>
#include <fstream>


using namespace std;

ifstream f1("B-large.in");
ofstream f2 ("1.out");

double XGoal, Cost, FarmGeneration;

/*double calc(double output)
{
    if(XGoal/output<(Cost/output)+XGoal/(output+FarmGeneration))
       return XGoal/output;
    else return (Cost/output+calc(output+FarmGeneration));
}*/
double calc()
{
    double output=2, time=0;
    while(XGoal/output>(Cost/output)+XGoal/(output+FarmGeneration))
    {
        time+=Cost/output;
        output+=FarmGeneration;
    }
    time+=XGoal/output;
    return time;
}
int main()
{


    int noCases, i;


    f1>>noCases;

    for(i=1; i<=noCases; i++)
    {
        f1>>Cost>>FarmGeneration>>XGoal;

        f2<<"Case #"<<i<<": ";
        f2<<setprecision(9)<<calc();

        f2<<"\n";
    }


    return 0;
}
