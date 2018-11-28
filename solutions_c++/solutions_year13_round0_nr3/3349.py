#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <sstream>

using namespace std;

// Fair and Square
inline bool isPalindrome(long long number)
{
	stringstream str;
	str << number;
	string rep = str.str();
	string::iterator iter_begin = rep.begin() ;
	string::iterator iter_end = rep.end() - 1;
	for (; iter_begin < iter_end; iter_begin++, iter_end-- )
	{
		if ( *iter_begin != *iter_end )
		{
			return false;			
		}
	}
	return true;
}

int main(void)
{
	ifstream input_file;
	input_file.open("round2/C-small-attempt0.in");

	int games;
	long long start;
	long long end;

	ofstream output_file;
	output_file.open("round2/output.out", std::ios_base::trunc);

	input_file >> games;
	for(int i = 0; i < games; i++)
	{
		input_file >> start >> end;
		int count = 0;
		long long s1 = sqrt((double)start);
		long long s2 = ceil(sqrt((double)end));
		for(long long iter = s1; iter <= s2; iter++)
		{
			long long square = iter * iter;
			if(square < start || square > end) continue;
			if(isPalindrome(iter) && isPalindrome(square)) count++;			
		}
		output_file << "Case #" << (i + 1) << ": " << count << endl;
	}

	input_file.close();
	output_file.close();

	return 0;
}