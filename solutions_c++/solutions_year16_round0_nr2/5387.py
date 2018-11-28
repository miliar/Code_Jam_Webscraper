#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

void remove_tail(string& s)
{
	int i;
	for (i = s.size() - 1; i >= 0; --i)
	{
		if (s[i] != '+')
			break;
	}

	s = s.substr(0, i+1);
}

void flip(string& s, int i)
{
	string temp = s.substr(0, i);
	reverse(temp.begin(), temp.end());
	for(int j = 0; j < temp.size(); ++j)
	{
		if (s[j] == '+')
			s[j] = '-';
		else
			s[j] = '+';
	};
}

int get_min_step(string s)
{
	remove_tail(s);
	int count = 0;

	while (s != "")
	{
		if (s.at(0) == '+' && s.at(1) != '+')
		{
			flip(s, 1);
			++count;
		}
			
		flip(s, s.size());
		++count;

		remove_tail(s);
	}

	return count;
}

int main()
{
	ifstream in_file("B-large.in");
	ofstream out_file("output.txt");

	if (in_file.is_open() && out_file.is_open())
	{
		string line;
		int i = 1, temp;
		in_file >> line;

		while (in_file >> line)
		{
			out_file << "Case #" << i << ": " << get_min_step(line) << endl;
			++i;
		}
	}

	in_file.close();
	out_file.close();

	return 0;
}
