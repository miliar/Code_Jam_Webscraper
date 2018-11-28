#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <limits>
#include <cassert>

using namespace std;

void flip(string& pancakes, int finish)
{
	//cout << "Flipping pancakes " << pancakes << " upto finish " << finish << endl;
	assert(finish >= 0 && finish < (int)pancakes.length());
	int start = 0;
	while (start <= finish)
	{
		char startChar = pancakes[start];
		char finishChar = pancakes[finish];
		startChar = (startChar == '-' ? '+' : '-');
		finishChar = (finishChar == '-' ? '+' : '-');
		pancakes[start] = finishChar;
		pancakes[finish] = startChar;
		start++; finish--;
	}
	//cout << "Flipped pancakes " << pancakes << endl;
}

int main(int argc, char** argv)
{
	ifstream input(argv[1]);
  unsigned long long T;
  input >> T;

  for (unsigned long long i = 1; i <= T; i++)
	{
		string pancakes;
		input >> pancakes;

		int finish = pancakes.length()-1;
		int flips = 0;
		while (finish >= 0)
		{
			if (pancakes[finish] == '+')
			{
				finish--;
				continue;
			}
			int start = 0;
			if (pancakes[start] == '-')
			{
				flip(pancakes, finish); flips++;
				assert(pancakes[finish] == '+');
				continue;
			}

			while (pancakes[start] == '+') start++;
			start--;
			flip(pancakes, start); flips++;
			assert(pancakes[start] == '-');
		}

		cout << "Case #" << i << ": " << flips << endl;
	}

  return 0;
}
