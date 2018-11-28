#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
	unsigned t;
	
	ifstream input("input.in");
	ofstream output("output.out");

	input >> t;

	unsigned k, c, s;

	for (int i = 1; i <= t; ++i)
	{
		input >> k >> c >> s;

		if (c == 1) 
			if( s == k) {
				output << "Case #" << i << ": ";
				for (int i = 0; i < k; i++)
					output << i + 1 << " ";
				output << endl;
				continue;
			} else {
				output << "Case #" << i << ": IMPOSSIBLE" << endl;
				continue;
			}

		if (k > 2 * c && k - c*2 > s - c) {
			output << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}

		int m = k;

		if( k % 2 == 0)
			if (s < k / 2) {
				output << "Case #" << i << ": IMPOSSIBLE";
				continue;
			}
			else;
		else
			if (s < k / 2 + 1) {
				output << "Case #" << i << ": IMPOSSIBLE";
				continue;
			}

		output << "Case #" << i << ": ";
		for (long long i = 2, j = 0; m > 0; i += 2, j += 2 * k)
			if (m != 1) {
				output << j + i << " ";
				m -= 2;
			} else {
				output << j + i - 1 << " ";
				m--;
			}

		output << endl;
	}

	input.close();
	output.close();

	return 0;
}