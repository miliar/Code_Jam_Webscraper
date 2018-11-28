#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string the_last_word(string s)
{
	string ret_ = "";
	for (char c : s)
	{
		if (ret_.size() == 0 || c < ret_[0])
		{
			ret_.push_back(c);
		}
		else
		{
			ret_.insert(ret_.begin(), c);
		}
	}
	return ret_;
}

int main(void)
{
	fstream input, output;
	input.open("A-large.in", ios::in);
	output.open("output.txt", ios::out);

	int t;
	input >> t;
	for (int i = 1; i <= t; i++)
	{
		string s;
		input >> s;
		output << "Case #" << i << ": " << the_last_word(s) << endl;
	}

	return 0;
}