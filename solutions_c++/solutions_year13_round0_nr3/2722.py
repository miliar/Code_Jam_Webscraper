#include <cctype>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>

#include <fstream>
#include <iostream>

#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <vector>
#include <utility>

using namespace std;







int main(void)
{
	int T;
	int n;

    unsigned long i;
    unsigned long lo, hi;
    unsigned long count;
    stringstream ss;
    string s;

	fstream input, output;

	input.open("C-small-attempt0.in", fstream::in);
	output.open("output.txt", fstream::out);

	if ( ! input.is_open() || ! output.is_open() )
	{
		cout << "well..." << endl;
		return -1;
	}

	input >> T;

	for ( n = 0; n < T; n++ )
	{
		input >> lo >> hi;
        
        count = 0;
        for ( i = ceil(sqrt(lo)); i <= floor(sqrt(hi)); i++ )
        {
            ss.str("");
            ss << i;
            s = ss.str();
            if (s == string(s.rbegin(), s.rend()))
            {
                ss.str("");
                ss << i*i;
                s = ss.str();
                if (s == string(s.rbegin(), s.rend()))
                    count++;
            }
        }

		output << "Case #" << n+1 << ": ";
		output << count << endl;
	}

	input.close();
	output.close();

	return 0;
}







/* */