#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <math.h>


using namespace std;

bool docheck ( unsigned int a )
{
	string n = to_string(a);
	int size = n.size();
	for(int i= 0 ; i< size; i++)
	{
		if ( n[i] != n[size-1-i] )
			return false;
	}
	return true;
}

int main(){
	ifstream in ("C-small-attempt0.in");
	ofstream out ("test.out" );

	int num;
	unsigned int from;
	unsigned int to;
	in >> num;
	for (int ii = 0; ii < num; ii++)
	{
		in >> from;
		in >> to;

		unsigned int p = sqrt(double(from));
		if ( p*p < from ) // min number that not less than 'from'
			p++;
		int count = 0;
		for(; p*p <= to ; p++)
		{
			// test if it's palindromes
			if ( docheck(p) )
				if ( docheck (p*p) )
					count++;
		}
		out <<"Case #"<<ii+1<<": "<< count<<endl;
	}
	return 0;
}