#include <bits/stdc++.h>

using namespace std;

struct Compare
{
	bool operator()(string& s1, string& s2)
	{
		return s1.size() > s2.size();
	}
};

isSubset(vector<char> v1, vector<char> v2)
{
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	return includes(v1.begin(), v1.end(), v2.begin(), v2.end());
}

int main()
{
	//vector<string> digits = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	vector<string> digits = {"ZERO", "SIX", "EIGHT", "FOUR", "SEVEN", "THREE", "FIVE", "NINE", "ONE", "TWO"};
	vector<string> digitsCopy = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	map<string, int> toInt;
	for(int i = 0; i < digitsCopy.size(); ++i)
		toInt.insert(make_pair(digitsCopy[i], i));

	Compare c;

	int t;
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase)
	{
		
		string input;
		cin >> input;
		vector<char> characterSet(input.begin(), input.end());
		string digitString = "";
		int i = 0;
		while(i < digits.size())
		{
			vector<char> digitSet(digits[i].begin(), digits[i].end());
			if(isSubset(characterSet, digitSet))
			{
				digitString += to_string(toInt[digits[i]]);
				for(auto x : digitSet)
				{
					auto it = find(characterSet.begin(), characterSet.end(), x);
					characterSet.erase(it);
				}
			}

				if(!isSubset(characterSet, digitSet)) ++i;
		}
		sort(digitString.begin(), digitString.end());
		cout << "Case #" << testCase << ": " << digitString << endl;
	}
}