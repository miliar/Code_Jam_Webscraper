#include <iostream>
#include<cstdio>

using namespace std;

double process();

int main() 
{
    int test;
    cin >> test;
    int i; // loop variable
    double result[test]; // results for each case
    for ( i = 0 ; i < test; i++)
    {
        result[i]=process();
    }
    
    //print results
    for (i = 0 ; i < test; i++)
    {
        cout << "Case #" << (i+1) << ": ";
        printf ("%.7f\n", result[i]);
    }
    return 0;
}

double process()
{
    double currentRate = 2.0;
    double time = 0, c, f, x, timeElasped = 0;
    double nt, newRate, bft; // new time, new rate, buy farm time
    cin >> c >> f >> x;
    while (true)
    {
        time = timeElasped + x/currentRate;
        //calculate time to (buy farm + new rate + time in new rate)
        bft = c / currentRate;
        if ((timeElasped + bft) > time)
        {
            break;
        }
        //calculate new rate, new time in new rate
        newRate = currentRate + f;
         // new time
        nt = timeElasped + bft + (x/newRate);
        //check
        if (nt < time)
        {
            //make the buy
            timeElasped = timeElasped + bft;
            currentRate = newRate;
        }
        else
        {
            break;
        }
    }
    return time;
}