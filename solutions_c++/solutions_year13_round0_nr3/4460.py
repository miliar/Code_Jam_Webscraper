#include <fstream>
#include <string>
#include <sstream>
using namespace std;

bool isPalindrome (int n)
{
	int i, j;
	string num = to_string(n);
	for (i = 0, j = num.length()-1; i < j; i++, j--)
	{
		if (num[i] != num[j])
			return false;
	}

	return true;
}

int nextPalindrome (int n)
{
	//naive method works for small inputs
	int next = n;
	while (true)
	{
		next++;

		if (isPalindrome(next))
			return next;
	}
}

int main (void)
{
	fstream input("C-small-attempt0.in");
	ofstream output("C-small-attempt0.out");

	int T;
	input >> T;

	for (int t = 1; t <= T; t++)
	{
		int min, max;
		input >> min;
		input >> max;

		//start at the lowest palindrome number and move up
		int count = 0;

		int pal = 0;
		int fs = 0;

		while (fs <= max)
		{
			if (fs >= min && isPalindrome(fs))
				count++;

			pal = nextPalindrome(pal);
			fs = pal * pal;
		}

		//output the result

		output << "Case #" << t << ": " << count;

		if (t != T)
			output << endl;
	}
}