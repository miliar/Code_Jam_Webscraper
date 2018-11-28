#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <math.h>
using namespace std;

int main (int argc, char * const argv[])
{
	freopen("input2.txt", "rt", stdin);
	freopen("output2.txt", "wt", stdout);
	
	int T;
	cin >> T;
	
    const double R = 2.0;
    for(int t = 0; t < T; t++)
    {
        double C, F, X;
        cin >> C;
        cin >> F;
        cin >> X;
        
        double last = X / R;
        int i = 1;
        while (1)
        {
            double v = 0.0;
            for (int j = 0; j < i; j++)
            {
                v += C / (R + (double)j * F);
            }
            v += X / (R + (double)i * F);
            if (v >= last)
                break;
            last = v;
            i++;
        }
        cout.setf(ios::showpoint);
        cout.precision(7);
        cout.setf(ios::fixed);
        
        cout << "Case #" << t+1 << ": " << last << endl;
        
	}
	
	return 0;
}

