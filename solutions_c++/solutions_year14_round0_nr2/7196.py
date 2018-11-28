#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<iomanip>
//#include<math.h>
//#include<utility>

using namespace std;

int main()
{
    cout.precision(10);
    int T;
    cin >> T;
    int cases = 0;
    for(int i = 0; i < T; i++)
    {
        cases++;
        double C, F, X;
        cin >> C >> F >> X;
        double maxtime = -1;
        double rate = 2, newrate = 2;
        double cha = -1;
        maxtime = X/rate;
        newrate = rate + F;
        double timeadded = C/rate;
        cha = X/newrate + C/rate;
        while(cha < maxtime)
        {
            maxtime = cha;
            rate = newrate;
            newrate = rate + F;
            timeadded += C/rate;
            cha = X/newrate + timeadded;
        }   
        cout << "Case #" << cases << ": ";
        if(cases < T)
            cout << maxtime << endl;
        else
            cout << maxtime;
    }
}
