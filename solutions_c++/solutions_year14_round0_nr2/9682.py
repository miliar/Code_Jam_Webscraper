#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    int test_cases,i;
    double x,c,f,r,time,ans;
    fstream inputfile("B-small-attempt4.in");
    fstream outputfile("output.txt");
    std::cout << std::setprecision(7) << std::fixed;
    outputfile.precision(10);
    inputfile >> test_cases;
    for(i=1;i<=test_cases;i++)
    {
    time = 0.0;
    r = 2.0;

    inputfile >> c;
    inputfile >> f;
    inputfile >> x;

    while(time + (x/r) > time + (c/r) + (x/(r+f)))
    {
        time += (c/r);
        r += f;
    }
    ans = (x/r) + time;

    outputfile <<"Case #" << i << ": "<<ans<<endl;
    }
        return 0;
}
