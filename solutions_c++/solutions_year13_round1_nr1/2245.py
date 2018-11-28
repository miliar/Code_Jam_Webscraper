#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <list>
#include <sstream>
#include <set>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

int main() 
{

    fstream f("in", fstream::in);
    int T;
    f >> T;
    for (int t = 1; t <= T; ++t) {
	long long R, P;
	f >> R >> P;
	// cout << R*R << " " << P << ",,,,,," << endl;
	/*
	int i = 1;
	while (i*(2*R+2*i-1) <= P) ++i;
    	cout << "Case #" << t << ": " << (i-1) << endl;
	*/

	double det = sqrt(4*R*R - 4*R + 8*P + 1);
	// cout << det << endl << endl;
	double r1 = ((1 - 2*R) + det)/4; 
	double r2 = ((1 - 2*R) - det)/4; 
	  // cout << r1 << endl;
	  // cout << r2 << endl;
	long long hi = r1 > r2 ? floor(r1) : floor(r2);
	long long f1 = floor(r1);
	long long f2 = floor(r2);
	 // cout << f1 << endl;
	 // cout << f2 << endl;
    	cout << "Case #" << t << ": " << hi << endl; 
    }
    return 0;

}
