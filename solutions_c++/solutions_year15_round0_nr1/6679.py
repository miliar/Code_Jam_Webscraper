#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int main(int argc, char* argv[])
{

	int testcases;
	cin >> testcases;
	
	for(int i = 0; i < testcases; i++)
	{
		int smax;
		string svals;
		cin >> smax;
		cin >> svals;

		int has = 0;
		int required = 0;

		for(int j = 0; j < svals.length(); j++)
		{
			if (has < j)
			{
				required += (j - has);
				has = j;
			}

			int cval = svals[j] - '0';
			has += cval;
		}

		cout << "Case #" <<(i+1) << ": " << required << endl;
	}


	return 0;
}
