#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
#include <map>
#include <set>

using namespace std;


int main()
{
    int cases, cnt = 1;
    double c, f, x;
    cin >> cases;
    
    cout.precision(7);
    cout.setf(ios::fixed);
    
    while(cases--)
    {
        double time = 0, n_farms = 0, t1, t2, t3;
        cin >> c >> f >> x;
        
        while(1)
        {
            t1 = x/(2 + f*n_farms);
            
            t2 = c/(2 + f*n_farms), t3 = x/(2 + f*(1+n_farms));
        
            if(t1 < (t2 + t3))
            {
                time += t1;
                break;
            }
            else
                time += t2, n_farms++;
        }
        cout << "Case #" << cnt++ << ": " << time << endl;
    }
    
    
    return 0;
}
