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
#include <functional>

using namespace std;

int main()
{
	unsigned nooftests;

	cin >> nooftests;

	for (unsigned i = 0; i < nooftests; ++i)
	{
		string inps;
		cin >> inps;
		string outs;

		outs = string(1, inps[0]);

		for (int i = 1; i < inps.size(); ++i)
		{
			if (inps[i] >= outs[0])
				outs = inps[i] + outs;
			else
				outs += inps[i];
		}
		cout << "Case #" << i + 1 <<": "<< outs << "\n";
	}

	return 0;
}