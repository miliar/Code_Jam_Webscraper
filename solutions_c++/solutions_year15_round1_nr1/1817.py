#include <iostream>
#include <fstream>
#include <cmath>
#define	INPUT_PATH	"C:\\In\\2015Round1A\\Q1\\A-large.in"
#define	OUTPUT_PATH	"C:\\In\\2015Round1A\\Q1\\A-large.out"
//#define	INPUT_PATH	"C:\\In\\2015Round1A\\Q1\\test.txt"
//#define	OUTPUT_PATH	"C:\\In\\2015Round1A\\Q1\\testout.txt"
int main()
{
	std::fstream f_in(INPUT_PATH, std::ios_base::in);
	std::fstream f_out(OUTPUT_PATH, std::ios_base::out);
	int num_of_cases;
	f_in >> num_of_cases;

	for (int i = 0; i < num_of_cases; ++i)
	{
		int result1 = 0;
		int result2 = 0;
		int eat_rate = 0;
		int n_mushrooms;
		f_in >> n_mushrooms;
		int* mushrooms = new int[n_mushrooms];
		for (int j = 0; j < n_mushrooms; ++j)
		{
			f_in >> mushrooms[j];
			if (j >= 1 && mushrooms[j] < mushrooms[j-1])
			{
				if (mushrooms[j - 1] - mushrooms[j] > eat_rate)
				{
					eat_rate = mushrooms[j - 1] - mushrooms[j];
				}
				result1 += mushrooms[j - 1] - mushrooms[j];
			}
		}
		for (int j = 0; j < n_mushrooms - 1; ++j)
		{
			if (mushrooms[j] <= eat_rate)
			{
				result2 += mushrooms[j];
			}
			else
			{
				result2 += eat_rate;
			}
		}
		f_out << "Case #" << (i + 1) << ": " << result1 << " " << result2 << "\n";
	}
}