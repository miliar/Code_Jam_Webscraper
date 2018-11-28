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

for(int h=0; h<tests; h++)
{
	int K, C, S;
	In >> K >> C >> S;
	Out << "Case #" << h+1 << ": " ;
	for(int i=1; i<=K; i++)
		Out << i << " ";

	Out << endl;

}

In.close();

Out.close();

return 0;

}
 
