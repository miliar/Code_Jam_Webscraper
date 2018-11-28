#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <vector>


/*


4
4 11111
1 09
5 110011
0 1


*/

int time_total(int number, int stack_size)
{
	if (number <= stack_size)
		return 0;

	int slices = number / stack_size;
	if (number % stack_size == 0)
		slices--;
	return slices;
}

int main (int argc, char* argv[])
{


	std::ifstream in(argv[1]);
	std::ofstream out("out.txt");

	if (!in || !out)
	{
		std::cout << "Input/output error." << std::endl;
		return(-1);
	}


	int test_count;
	in >> test_count;

	for(int i = 0; i < test_count; ++i)
	{
		std::vector<int> diners;
		int diners_count;
		
		in >> diners_count;
		diners.resize(diners_count);
		for (int n = 0; n < diners_count; ++n)
		{
			in >> diners[n];
		}

		std::sort(diners.begin(), diners.end());
		std::vector<int> times;
		times.resize(diners.back() + 1);
		times[0] = 0;
		for(int n = 1; n <= diners.back(); ++n)
		{
			for(int d = 0; d < diners_count; ++d)
				times[n] += time_total(diners[d], n);
			times[n] += n;
		}		
		std::sort(times.begin(), times.end());

		out << "Case #" << i + 1 << ": " << times[1] << std::endl;
	}

	in.close();
	out.close();

	return 0;
}