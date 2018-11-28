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

cout << tests << endl;

for(int h=0; h<tests; h++)
{
	int N;
	In >> N;
	cout << h+1 << " " << N << endl;

	vector<bool> seen(10, false);

	int original = N;
	
	if(N==0)
		Out << "Case #" << h+1 << ": INSOMNIA" <<  endl;
	else
	{
		int digitsLeft = 10;
		N = 0;
		while(digitsLeft > 0)
		{
			N += original;
			int temp = N;
			do
			{
				int t = temp % 10;
				if( !seen[t] ) digitsLeft--;
				seen[t] = true;
				temp /= 10;
			}
			while(temp);
		}


		Out << "Case #" << h+1 << ": " << N << endl;
	}
}

In.close();

Out.close();

return 0;

}
 
