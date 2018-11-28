#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int tc, tnum = 0;
	cin >> tc;
	
	fstream file("BullsEye.txt", iostream::out);

	while (tnum < tc)
	{
		long long r, t;
		cin >> r >> t;

		long long sum = 0, count = 0;

		while (sum < t)
		{
			sum += 2*r+1;
			r += 2;

			if (sum <= t)
				++count;
		} 

		file << "Case #" << tnum+1 << ": " << count << endl;
		++tnum;
	}
}