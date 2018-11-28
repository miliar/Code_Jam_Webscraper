#include <iostream>
#include <utility> 
#include <string>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;


int main(int argc, char* argv[])
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	
	int T;
	in >> T;
	for (int t = 1; t <= T; ++t)
	{
		int n;
		in >> n;
		vector<int> mushrooms;
		mushrooms.reserve(n);
		int count;
		for (int i = 0; i < n; ++i)
		{
			in >> count;
			mushrooms.push_back(count);
		}

		int sum1 = 0;
		int sum2 = 0;

		if (n >= 2)
		{
			int maxd = 0;
			for (int i = n - 2; i >= 0; --i)
			{
				int d = mushrooms[i] - mushrooms[i + 1];
				if (d > 0)
				{
					sum1 += d;
					if (d > maxd)
						maxd = d;
				}
			}
			for (int i = 0; i < n - 1; ++i)
				sum2 += mushrooms[i] > maxd ? maxd : mushrooms[i];

		}

		out << "Case #" << t << ": " << sum1 << " " << sum2 << endl;
	}

	return 0;
}