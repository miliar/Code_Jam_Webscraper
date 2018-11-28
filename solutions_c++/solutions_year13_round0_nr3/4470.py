#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define NUM_MAX 100000000

std::vector<unsigned long long> output;

int isPalindrome(unsigned long long num)
{
	unsigned long long n = num;
	unsigned long long reversed = 0;

	while (n > 0)
	{
		reversed = reversed * 10 + n % 10;
		n /= 10;
	}

	if (num == reversed)
	{
		return true;
	}

	return false;
}

void alg()
{
	long long min, max;
	cin >> min;
	cin >> max;
	for (long i = 1; i < NUM_MAX; i++)
	{
		if (isPalindrome(i))
		{
			unsigned long long x = i * i;
			if (x > max)
			{
				break;
			}
			if (isPalindrome(x))
			{
				output.push_back(x);
			}
		}
	}

	int count = 0;
	for (vector<unsigned long long>::iterator iter = output.begin(); iter != output.end(); ++iter)
	{
		if (((*iter) >= min) && ((*iter) <= max))
		{
			count++;
		}
	}
	cout << count << endl;
}

int main()
{
	int d;
	cin >> d;
	for (int case_no = 1; case_no <= d; ++case_no) {
		cout << "Case #" << case_no << ": ";
		alg();
		output.clear();
	}
	return 0;
}
