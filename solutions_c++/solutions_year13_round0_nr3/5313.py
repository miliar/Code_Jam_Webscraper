//Standard libraries
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <cmath>
#include <sstream>

using namespace std;

bool is_palindrome(string num)
{
	int size = num.length();
	
	if (size == 1)
		return true;

	for (int i = 0; i < (size/2); ++i)
	{
		if (num[i] != num[size - 1 -i])
			return false;
	}
	return true;
}

string itostr(unsigned long long int num)
{
	ostringstream converter;
	converter << num;

	return converter.str();
}

unsigned long long int _find_root(unsigned long long int num,
								 unsigned long long int begin, 
								 unsigned long long int end)
{
	unsigned long long int mid = (end - begin);
	mid = mid>>1;
	mid = begin + mid;

	if (begin >= end)
		return mid;
	
	if (mid * mid == num)
		return mid;
	else if (mid * mid > num)
		return _find_root(num, begin, mid - 1);
	else if (mid * mid < num)
		return _find_root(num, mid + 1, end);
}

unsigned long long int find_root(unsigned long long int num)
{
	if (num <= 1)
		return num;

	return _find_root(num, 0, num);
}

int main(int argc, char*argv[])
{
	ifstream file;
	file.open(argv[1]);

	int T;
	file >> T;

	unsigned long long int A, B;
	int count = 0;

	for (int j = 0; j < T; ++j)
	{
		count = 0;
		file >> A;
		file >> B;

		for(unsigned long long int i = 1; i <= B; ++i)
		{
			if (is_palindrome(itostr(i)))
			{
				if (is_palindrome(itostr(i * i)) && ( (i * i) <= B) && ( (i * i) >= A))
				{
					++count;
				}
			}
		}
		cout << "Case #" << j+1 << ": " << count << endl;
	}

	return 0;
}
