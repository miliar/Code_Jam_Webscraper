#include <cmath>
#include <cstdlib>
#include <cstdio>

#include <iostream>

#define PI 3.14159265359

using namespace std;

int main(void)
{
	int T;
	cin >> T;
    
    int x;
    long long ring, paint;

	for ( int n = 0; n < T; n++ )
	{
		cin >> ring >> paint;
        
        x = 0;
        
		for ( ;; )
        {
            paint -= 2*ring+1;
            if (paint < 0)
                break;
            else
                x++;
                ring += 2;
        }

		cout << "Case #" << n+1 << ": ";
		cout << x << endl;
	}
	return 0;
}