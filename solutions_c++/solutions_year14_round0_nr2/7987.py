#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
 
using namespace std;
 
int main()
{
    int cases;
     
    while(cin >> cases)
    {
    	for (int i = 0; i < cases; ++i)
        {
            double c, f, x;
            double your_cookies = 0;
            double total_time = 0;
            double rate = 2;

            cin >> c >> f >> x;

            double temp;
            double estimated = x/rate;

            while(true)
            {
                if(estimated <= (x/(rate+f))+(c/rate))
                {
                    total_time += estimated;
                    break;
                }

                temp = c - your_cookies;
                your_cookies += temp;

                total_time += your_cookies/rate;

                if(your_cookies >= c)
                {
                    your_cookies -= c;
                    rate += f;
                }

                estimated = (x/rate);
            }

            cout << "Case #" << i+1 << ": ";

            cout << setprecision(7) << fixed << total_time << endl;    
        }
        
    }
     
    return 0;
}