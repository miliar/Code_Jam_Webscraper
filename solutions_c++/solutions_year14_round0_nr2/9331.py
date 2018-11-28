/*
ID: enggi231
LANG: C++
PROG: 
 */

#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <iomanip>

#define ll long long

using namespace std;

fstream out;
long double c, f, x, T, mtim = 1000000;

vector<int> ans;


long double t(long double cur, long double r, long double ct) {
    cout<< cur <<" "<< r << endl;
    if (ct > mtim)
        return 1000000;
    if (cur >= x) 
        return 0;
    if (cur >= c) 
        return min(t(cur-c, r+f, ct), (x-cur)/r);
    if (mtim > ct + (x-cur)/r)
        mtim = ct + (x-cur)/r;
    if (mtim > (c-cur)/r + t(0, r+f, ct+(c-cur)/r))
        mtim = (c-cur)/r + t(0, r+f, ct+(c-cur)/r);
    return min((x-cur)/r, (c-cur)/r + t(0, r+f, ct+(c-cur)/r));
}

int main()
{
	cin >> T;
    cout << fixed << setprecision(7);
    for (int i = 1; i <= T; i++) {
        cin >> c >> f >> x;
        
       // t(0.0, 2.0, 0);
        //cout  << "Case #" << i <<": "<< t(0.0, 2.0, 0) <<endl;
        
        double t1 = 0, t2 = 0, m = 1000000;
        for (int n = 0; n < 50000; n++) {
            
            t2 = x/(2.0+n*f);
            //cout << t1+t2 << endl;
            
            m = min(m, t1+t2);
            
            t1 += c/(2.0+n*f);
            
        }
        
        cout  << "Case #" << i <<": "<< m <<endl;
    
    }
    
	return 0;
}

