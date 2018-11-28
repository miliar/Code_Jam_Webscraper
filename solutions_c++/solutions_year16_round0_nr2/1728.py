// 2016QualificationRound.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>

using namespace std;

bool IsDone(const string& s)
{
	return all_of(s.cbegin(), s.cend(), [](auto c) { return c == '+'; });
}

template<class It>
void Flip(It from, It to)
{
	for (auto it = from; it != to; ++it)
	{
		if (*it == '+')
			*it = '-';
		else
			*it = '+';
	}

	reverse(from, to);
}

void PlusTop(string& s)
{
	auto it = find(s.begin(), s.end(), '-');
	Flip(s.begin(), it);
}

void MinusTop(string& s)
{
	auto it = find(s.rbegin(), s.rend(), '-');
	Flip(s.begin(), it.base());
}

int main()
{
	std::ifstream fs("data/B-large.in");

	int t;

	fs >> t;
	string foo;
	getline(fs, foo);

	for(auto i = 1; i <= t; i++)
	{
		string s;
		getline(fs, s);

		auto count = 0;

		while (!IsDone(s))
		{
			if (s[0] == '+')
				PlusTop(s);
			else
				MinusTop(s);
			count++;
		}

		cout << "Case #" << i << ": " << count << endl;
	}

    return 0;
}

