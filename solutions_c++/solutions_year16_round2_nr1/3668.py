#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

unordered_map<string, int> numbers = { make_pair("ZERO", 0), 
									   make_pair("ONE", 1),
									   make_pair("TWO", 2),
									   make_pair("THREE", 3),
									   make_pair("FOUR", 4),
									   make_pair("FIVE", 5),
									   make_pair("SIX", 6),
									   make_pair("SEVEN", 7),
									   make_pair("EIGHT", 8),
									   make_pair("NINE", 9) };

int exclude(string s, string excludeString, string& result)
{
	for (int i = 0; i < excludeString.size(); ++i)
	{
		if (s.find(excludeString.at(i)) == string::npos)
			return -1;

		s.erase(s.find(excludeString.at(i)), 1);
	}
	
	result = s;
	return 0;
}

bool containsChar(string s, char c)
{
	for (int i = 0; i < s.size(); ++i)
		if (s.at(i) == c)
			return true;

		return false;
}

vector<string> getPossibleNumbers(char c)
{
	vector<string> result;
	for (auto it = numbers.begin(); it != numbers.end(); ++it)
	{
		if (containsChar(it->first, c))
			result.push_back(it->first);
	}

	return result;
}

int getPhoneNumber(string s, vector<int>& nums)
{
	if (s.size() == 0)
		return 0;

	int size = nums.size();
	vector<string> ns = getPossibleNumbers(s.at(0));
	for (int j = 0; j < ns.size(); ++j)
	{
		nums.push_back(numbers[ns[j]]);
		string result;
		if (exclude(s, ns[j], result) == -1)
			nums.pop_back();
		else
		{
			int ret = getPhoneNumber(result, nums);
			if (ret == 0)
				return 0;

			if (ret == -1)
				nums.pop_back();
		}
	}

	if (nums.size() == size)
		return -1;

	return 0;
}

int main()
{
	ifstream in_file("A-small-attempt0.in");
	ofstream out_file("output.txt");

	if (in_file.is_open() && out_file.is_open())
	{
		string line;
		int i = 1, temp;
		getline(in_file, line);

		while (getline(in_file, line))
		{
			vector<int> phoneNumber;
			getPhoneNumber(line, phoneNumber);

			sort(phoneNumber.begin(), phoneNumber.end());
			out_file << "Case #" << i << ": ";
			for (int i = 0; i < phoneNumber.size(); ++i)
			{
				out_file << phoneNumber[i];
			}
			out_file << endl;
			++i;
		}
	}

	in_file.close();
	out_file.close();

	return 0;
}