/*
	https://code.google.com/codejam/contest/2418487/dashboard#s=p0
*/
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    int T;
	long long r, t;
    
    cin >> T;
    
    for (int i = 0; i < T; i++) {
		cin >> r;
		cin >> t;
		
		//cout << "r: " << r << " t: " << t << endl;
	
		long long tmp = floor(sqrt(pow(2 * r - 1, 2) + 8 * t));
		//cout << "tmp: " << tmp << endl;
		
		tmp = tmp + (1 - 2 * r);
		//cout << "tmp: " << tmp << endl;
		
		tmp = floor(tmp / 4);
		//cout << "tmp: " << tmp << endl;
		
		cout << "Case #" << (i + 1) << ": " << tmp << endl;
    }

    return 0;
}
