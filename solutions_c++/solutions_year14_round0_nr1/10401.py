#include <iostream>
#include <cstdio>
#include <unordered_set>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;

unordered_set<int> read_cards(int row)
{
	unordered_set<int> results;
	//cout << "reading cards from row\n";
	for(int i = 0; i < 4; ++i)
	{
		string line;
		getline(cin, line);
		//cout << line << endl;
		//cout << "getting row " << i << " should get " << row << endl;

		if(i != row)
			continue;
		istringstream is(line);
		for(int j = 0; j < 4; ++j)
		{
			int number;
			is >> number;
			//cout << "read number " << number << endl;

			results.insert(number);
		}
	}
	return results;
}

int solve()
{
	int first, second;
	cin >> first;
	cin.get();
	//cout << "first row is " << first << endl;
	auto first_line = read_cards(first - 1);
	cin >> second;
	cin.get();
	//cout << "second row is " << second << endl;

	auto second_line = read_cards(second - 1);
	int count = 0, number = 0;
	for_each(first_line.begin(), first_line.end(), [&] (int element)
	{
		if(second_line.count(element))
		{
			++count;
			number = element;
		}
	});
	if(count == 0)
	{
		return 0;
	}
	else if(count > 1)
	{
		return -1;
	}
	return number;
}

int main()
{
	int tests;
	cin >> tests;
	//cout << " there will be " << tests << " tests\n";
	for(int i = 0; i < tests; ++i)
	{
		int res = solve();
		cout << "Case #" << (i + 1) << ": ";
		if(res < 0)
		{
			cout << "Bad magician!";
		}
		else if(res == 0)
		{
			cout << "Volunteer cheated!";
		}
		else
		{
			cout << res;
		}
		cout << endl;
	}
}