#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <map>
#include <cctype>
#include <math.h>
#include <numeric>
#include <set>
#include <stack>
#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	unsigned nooftests;
	string instack;
	cin >> nooftests;

	for (unsigned i = 0; i < nooftests; ++i)
	{
		cin >> instack;
		string tststack = instack;
		unsigned cnt = 0;
		bool done = false;

		while (true)
		{
			size_t minuspos = tststack.find_last_of("-");
			
			if (minuspos == 0)
			{
				cnt += 1;
				done = true;
				break;
			}
			else if (minuspos!=std::string::npos)
			{
				if (tststack[0] == '-')
				{
					string tstcpy = tststack;
					for (size_t j = 0; j <=minuspos; ++j)
					{
						if (tststack[minuspos - j] == '+')
							tstcpy[j] = '-';
						else
							tstcpy[j] = '+';
					}
					tststack = tstcpy;
					cnt += 1;
				}
				else if (tststack[0] == '+')
				{
					size_t pluspos = 0;
					while ((tststack[pluspos] == '+') && (pluspos<minuspos)){
						tststack[pluspos] = '-';
						pluspos += 1;
					}
					cnt += 1;
				}
			}
			else if (minuspos == std::string::npos)
			{
				done = true;
				break;
			}
		}
		if (done)
			cout << "Case #" << i + 1 << ": " << cnt<<"\n";		
	}
	return 0;
}