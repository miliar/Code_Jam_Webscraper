#include <iostream>
#include <string>

using namespace std;

int min_flip(const char *str, unsigned int size)
{
	string reduction;

	reduction.push_back(str[0]);
	for(unsigned int i = 1; i < size; ++i)
	{
		char last = str[i - 1];
		if(str[i] != last)
			reduction.push_back(str[i]);
	}

	int flips = reduction.size();
	if(reduction[reduction.size() - 1] == '+')
		flips -= 1;

	return flips;
}

int main()
{
	unsigned int T;
	cin >> T;

	for(unsigned int i = 0; i < T; ++i)
	{
		string testcase;
		cin >> testcase;

		cout << "Case #" << i+1 << ": " << min_flip(&testcase[0], testcase.size()) << '\n';
	}
}
