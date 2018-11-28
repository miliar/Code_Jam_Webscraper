#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
    int n;
    cin>>n;
    
    for (int i=0; i<n; i++)
    {
       double c,f,x;
       cin>>c>>f>>x;
       
       double cookiesPerSecond = 2.0;
       double totalCookies = 0.0;
       double totalTime = 0.0;
       
       while ( (x-c)/cookiesPerSecond > (x/(cookiesPerSecond+f)) )
       {
          totalTime += c/cookiesPerSecond;
          cookiesPerSecond += f;
       }
       
       totalTime += (x)/cookiesPerSecond;
       
       cout << "Case #" << i+1 << ": " << fixed << setprecision(7) << totalTime << endl;
       
    }
};


