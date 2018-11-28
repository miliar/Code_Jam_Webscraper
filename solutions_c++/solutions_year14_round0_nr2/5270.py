#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    string line;
    getline(cin,line);
    stringstream firstline(line);
    int numbertestcases;
    firstline >> numbertestcases;
    double c,f,x;
    double ncookies;
    double speed;
    double time;
    double completetime;
    double totaltime = 0;
    for(int m=1;m<=numbertestcases;m++)
    {
        getline(cin,line);
        stringstream testline(line);
        testline >> c;
        testline >> f;
        testline >> x;
        ncookies = 0.0;
        speed = 2.0;
        time = 0.0;
        totaltime = 0.0;
        while(true)
        {
            //time until next farm can be bought
            time = c/speed;
            //time until enough cookies
            completetime = (x-ncookies)/speed;
            if (completetime<=time)
            {
                totaltime += completetime;
                break;
            }
            totaltime += time;
            ncookies += c;
            if ((x/(speed+f))<((x-c)/speed))
            {
                //buy a new farm
                ncookies -= c;
                speed += f;
            }
        }
        cout << fixed;
        cout.precision(7);
        cout << "Case #" << m << ": " << totaltime << endl;
    }
    return 0;
}
