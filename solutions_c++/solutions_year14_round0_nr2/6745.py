#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main (void)
{
    ifstream cin ("B-large.in");
    ofstream cout ("out.txt");
    
    int t;
    cin >> t;
    
    cout.precision(8);
    
    for (int i = 0; i < t; i++)
    {
        double c, f, x;
        cin >> c >> f >> x;
        
        double t = 0;
        double curCookies = 0, curRate = 2;
        
        if (c >= x)
            t = x/2;
        else
        {
            while (c/curRate + x/(curRate+f) < x/curRate)
            {
                t += c/curRate;
                curRate += f;
            }
            
            t += x/curRate;
        }
            
        cout << "Case #" << i+1 << ": ";
        cout << fixed << t << endl;
    }
          
   // while (true) {}  
    return 0;
}
