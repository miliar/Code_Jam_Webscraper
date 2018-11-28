#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	int cases;
	cin >> cases;

	for(int i=1; i<=cases; i++)
	{
		string retval;
		string input;
		cin >> input;

		retval = input[0];
		for(size_t j=1; j<input.size(); j++)
		{
			if(input[j] >= retval[0])
			{
				retval = input[j] + retval;
			}
			else
			{
				retval += input[j];
			}
		}


		cout << "Case #" << i << ": " << retval << endl;
	}

	return 0;
}
