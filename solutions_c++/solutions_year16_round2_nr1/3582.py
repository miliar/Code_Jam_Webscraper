#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <fstream>
#include <vector>

using namespace std;

vector<string> digits = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
map<string, char> strToDigits;
map<char, int> sCount;
vector< map<char, int> > dCount;
bool finished = false;
string result = "";

bool isConsumed(map<char, int> m)
{
	for (char i = 'A'; i <= 'Z'; i++)
	{
		if (m[i] > 0)
			return false;
	}
	return true;
}

bool canSubtract(map<char, int> s, map<char, int> d)
{
	for (char i = 'A'; i <= 'Z'; i++)
	{
		if (d[i] > s[i])
			return false;
	}
	return true;
}

map<char,int> subtract(map<char,int> s, map<char, int> d)
{
	map<char, int> res;
	for (char i = 'A'; i <= 'Z'; i++)
	{
		res[i] = s[i] - d[i];
	}
	return res;
}

void solve(map<char,int> curCount, string res)
{
	if (finished)
		return;

	if (isConsumed(curCount))
	{
		finished = true;
		result = res;
	}

	for (int i = 0; i < dCount.size(); i++)
	{
		if (canSubtract(curCount, dCount[i]))
		{
			map<char, int> nCount = subtract(curCount, dCount[i]);
			solve(nCount, res + ((char)(i + '0')));
		}
	}
}

int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("output.txt");
	
	for (int i = 0; i < digits.size(); i++)
	{
		strToDigits[digits[i]] = ('0' + i);
		map<char, int> cdCount;
		for (int j = 0; j < digits[i].size(); j++)
		{
			cdCount[digits[i][j]]++;
		}
		dCount.push_back(cdCount);
	}

	int n;
	cin >> n;

	for (int ci = 1; ci <= n; ci++)
	{
		string s;
		cin >> s;
		finished = false;
		sCount.clear();

		for (int j = 0; j < s.size(); j++)
		{
			sCount[s[j]]++;
		}

		solve(sCount, "");
		sort(result.begin(), result.end());
		cout << "Case #" << ci << ": " << result << endl;

	}

}