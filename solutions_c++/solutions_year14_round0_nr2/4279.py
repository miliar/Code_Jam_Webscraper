/*
 ID: sarahwo1
 PROG: humble
 LANG: C++
 */
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <cctype>
#include <streambuf>
#include <string>
#include <sstream>
#include <cmath>
#include <stack>
//#include <queue>
#include <ctime>
#include <time.h>
#include <iomanip>
#include <set>

using namespace std;
#define INF (2147483630);



int main()
{
    ofstream cout("/Users/sarahwooders/Desktop/money.txt");
    ifstream cin("/Users/sarahwooders/Desktop/text.txt");
    
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; i ++)
    {
        double factoryCost;
        double factoryRate;
        double goal;
        cin >> factoryCost;
        cin >> factoryRate;
        cin >> goal;
        
        double rate = 2;
        double time = 0;
        double curr = 0;
        
        while (true)
        {
            if(curr >= factoryCost)
            {
                if((goal - curr + factoryCost)/(rate + factoryRate) < (double)(goal - curr)/rate)
                {
                    rate += factoryRate;
                    curr -= factoryCost;
                }
                else
                {
                    time += (double)(goal - curr)/rate;
                    curr = goal;
                    break;
                }
            }
            else
            {
                if(factoryCost - curr < goal - curr)
                {
                    time += (double)(factoryCost - curr)/rate;
                    curr = factoryCost;
                }
                else
                {
                    time += (double)(goal - curr)/rate;
                    curr = goal;
                    break;
                }
            }
            
        }
        cout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << time << endl;
    }
}

