#include <iostream>
#include <cstdio>
#include <fstream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void problemA()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	vector<string> consists = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
	vector<pair<char, int>> deter;
	deter.push_back(make_pair('Z', 0));
	deter.push_back(make_pair('W', 2));
	deter.push_back(make_pair('U', 4));
	deter.push_back(make_pair('X', 6));
	deter.push_back(make_pair('G', 8));
	deter.push_back(make_pair('T', 3));
	deter.push_back(make_pair('O', 1));
	deter.push_back(make_pair('F', 5));
	deter.push_back(make_pair('S', 7));
	deter.push_back(make_pair('E', 9));

	int T;
	in >> T;
	for (int t = 1; t <= T; t++)
	{
		string phone;
		in >> phone;

		map<char, int> counts;
		for (int i = 0; i < phone.size(); i++)
			counts[phone[i]] += 1;

		vector<int> numbers;
		for (auto iter = deter.begin(); iter != deter.end(); ++iter)
		{
			char target = iter->first;
			int number = iter->second;
			int count = counts[target];
			if (count > 0)
			{
				for (int i = 0; i < count; i++)
					numbers.push_back(number);
				
				for (int i = 0; i < consists[number].size(); i++)
					counts[consists[number][i]] -= count;
			}
		}


		//cout << "T" << endl;
		//for (auto iter = counts.begin(); iter != counts.end(); ++iter)
		//	cout << iter->first << ":" << iter->second << endl;

		out << "Case #" << t << ": ";
		sort(numbers.begin(), numbers.end());
		for (int i = 0; i < numbers.size(); i++)
			out << numbers[i];
		out << endl;
	}

	in.close();
	out.close();
}

int main(int argc, char**argv)
{
	problemA();
	return 0;
}