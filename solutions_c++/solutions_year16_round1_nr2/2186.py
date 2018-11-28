#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
	fstream input, output;
	input.open("B-large.in", ios::in);
	output.open("output.txt", ios::out);
	int t;
	input >> t;
	for (int i = 1; i <= t; i++)
	{
		int N;
		int count[3000];
		input >> N;
		memset(count, 0, sizeof(count));
		int total = N*(2 * N - 1);
		int maxVal = -1;
		for (int k = 0; k < total; k++)
		{
			int h;
			input >> h;
			if (h > maxVal)
				maxVal = h;
			count[h]++;
		}
		output << "Case #" << i << ":";
		for (int k = 0; k <= maxVal; k++)
		{
			if (count[k] > 0 && count[k] % 2 == 1)
				output << " " << k;
		}
		output << endl;

	}
	
}