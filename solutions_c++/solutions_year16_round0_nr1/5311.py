#include <fstream>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

set<int> get_digit(int N)
{
	set<int> digits;
	while (N)
	{
		digits.insert(N%10);
		N /= 10;
	}

	return digits;
}

int get_max_number(int N)
{
	int digits_mask = 0, i = 1, temp;
	set<int> digits;

	while (digits_mask != 1023)
	{
		temp = N * i;
		digits = get_digit(temp);
		for_each(digits.begin(), digits.end(), [&digits_mask](int d){
			if (!(digits_mask & (1 << d)))
				digits_mask |= 1 << d;
		});

		++i;
	}

	return N*(--i);
}

int main()
{
	ifstream in_file("A-large.in");
	ofstream out_file("output.txt");

	if (in_file.is_open() && out_file.is_open())
	{
		string line;
		int i = 1, temp;
		in_file >> line;

		while (in_file >> line)
		{
			temp = stoi(line);

			if (temp == 0)
				out_file << "Case #" << i << ": INSOMNIA" << endl;
			else
				out_file << "Case #" << i << ": " << get_max_number(temp) << endl;
			++i;
		}
	}

	in_file.close();
	out_file.close();

	return 0;
}
