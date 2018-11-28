#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <limits>

using namespace std;

void updateNumsSeen(unsigned long long N, vector<bool>& nums, unsigned long long& numsSeen)
{
	while (N)
	{
		unsigned long long digit = N % 10;
		N /= 10;
		if (nums[digit]) continue;
		nums[digit] = true;
		numsSeen++;
	}
	return;
}

int main(int argc, char** argv)
{
	ifstream input(argv[1]);
  unsigned long long T;
  input >> T;

  for (unsigned long long i = 1; i <= T; i++)
	{
		unsigned long long N;
		input >> N;

		vector<bool> nums(10, false);
		unsigned long long numsSeen = 0;
		unsigned long long multiplier = 1;
		unsigned long long step = N;
		while (N)
		{
			updateNumsSeen(N, nums, numsSeen);
			if (numsSeen == 10) break;
			multiplier++;
			N += step;
		}
		if (numsSeen < 10)
		{
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << N << endl;
		}
	}

  return 0;
}
