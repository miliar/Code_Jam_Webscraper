#include <string.h>       
#include <vector>       
#include <set>       
#include <map>       
#include <algorithm>       
#include <math.h>       
#include <sstream>       
#include <ctype.h>       
#include <queue>       
#include <stack>       
#include <iostream> 
#include <gmp.h>	// if GMP is not allowed, I apologize
#include <fstream>
using namespace std;

int main(int argc, char** argv)
{

string fName = argv[1];

fstream In((fName+".in").c_str(), ios::in);
fstream Out((fName + ".out").c_str(), ios::out);

int tests;

In >> tests;

int N, M;

for(int h=0; h<tests; h++)
{
	long double C, F, X, temp;
	In >> C >> F >> X;
	long double cookiesum = 2;
	long double best = X / 2.0;
	long double elapsedtime = 0;
	while(true)
	{
		elapsedtime += C / cookiesum;
		cookiesum += F;
		temp = elapsedtime + X / cookiesum;
		if(temp > best) break;
		//cout << elapsedtime << " " << cookiesum << " " << temp << ' ' << best << endl;
		best = temp;
	}
	//cout << h+1 << " " << best << endl;
	//cin >> elapsedtime;
	Out.precision(12);
	
	Out << "Case #" << h+1 << ": " << best << endl;

}

In.close();

Out.close();

return 0;

}
 
