#include <iostream>
#include <vector>
using namespace std;

typedef unsigned long long uint64;
int main(int argc, char* argv[])
{
	int T;
	cin >> T;

	for (int caseId = 1; caseId <= T; caseId++)
	{
		uint64 r, t;
		cin >> r >> t;

		uint64 n = 0;
		uint64 curr = 2*r+1;
		//uint64 sum = 2*n*n+(2*r+1)*n;
		uint64 sum = curr;

		while (t >= sum)
		{
			n++;
			curr += 4;
			sum += curr;
		}

		cout << "Case #" << caseId << ": " << n << endl;
	}

	return 0;
}

