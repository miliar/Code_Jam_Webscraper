#include <iostream>
#include <string>
//#include <vector>
//#include <unordered_map>
//#include <algorithm>
//#include <functional>

using namespace std;



/*
We can normalize the group of sequence:
Let s = "--+-"
s can be "-+-"

What does it mean?

If the first character is "-", then increase +1
If "-" character is in the middle of sentence(between "+" characters), then increase +2

Thus, the algorithm is can be simplified like,
1. remove "-" signs in front of the string and +1, if it exists
2. scan the rest string and +2 if "-" exists
*/

void execute()
{
	// Input
	string pattern;
	cin >> pattern;

	int flip = 0, pivot = 0, len = pattern.length();
	
	// remove the front "-" sign and increase one
	while (pivot < len && pattern[pivot] == '-')
	{
		flip = 1;
		pivot++;
	}

	// Scan the rest
	while (pivot < len)
	{
		if (pattern[pivot] == '-')
		{
			flip += 2;

			// remove the rest '-'s because the contiguous '-' sequence can be normalized to one '-'
			while (pivot + 1 < len && pattern[pivot + 1] != '+') pivot++;
		}
		pivot++;
	}


	cout << flip << endl;
}

void printHeader(int num)
{
	cout << "Case #" << num << ": ";
}

int main()
{
	int loop;
	cin >> loop;

	for (int i = 1; i <= loop; i++)
	{
		printHeader(i);
		execute();
	}
}