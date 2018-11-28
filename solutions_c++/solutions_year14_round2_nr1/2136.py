#include <iostream>
#include <string>
#include <vector>

#pragma warning(disable: 4996)

using namespace std;

vector<vector<int>> ints;

string minStr(string str, int number)
{
	string res = "";
	int index = 0, c = 1;
	bool b = true;
	for (int i = 0; i<str.length()-1; i++)
	{
		b = str[i]!=str[i+1];
		if (b)
		{
			ints[number].push_back(c);
			c = 1;
			res += str[i];
			index++;
		} else
			c++;
	}
	res += str[str.length()-1];
	ints[number].push_back(c);
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Tests;
	cin >> Tests;
	for (int i = 0; i<Tests; i++)
	{
		int N;
		cin >> N;
		vector<string> strs(N);
		ints.clear();
		ints.resize(N);
		for (int j = 0; j<N; j++)
		{
			cin >> strs[j];
			strs[j] = minStr(strs[j], j);
		}
		if (strs[0]!=strs[1])
			cout << "Case #" << i+1 << ": " << "Fegla Won" << endl;
		else
		{
			int res = 0;
			for (int j = 0; j<strs[0].length(); j++)
				res += abs(ints[0][j]-ints[1][j]);
			cout << "Case #" << i+1 << ": " << res << endl;
		}
	}
	return 0;
}
