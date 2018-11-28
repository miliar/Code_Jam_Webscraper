#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

void print(vector<string> substrings)
{
	for (vector<string>::iterator it = substrings.begin(); it < substrings.end(); it++)
	{
		cout << *it << " ";
	}
	cout << endl;
}

bool IsConsonant(char c);

struct substring
{
	string substr;
	int start;
};

int main()
{
	int numCases;
	cin >> numCases;
	for (int caseNum = 1; caseNum <= numCases; caseNum++)
	{
		string word;
		cin >> word;
		int n;
		cin >> n;
		int start = 0;
		int len = n;
		vector<substring> substrings;
		while (len <= word.size())
		{
			while (start <= word.size() - len)
			{
				string substr = word.substr(start, len);
				substring sub;
				sub.substr = substr;
				sub.start = start;
				substrings.push_back(sub);
				start++;
			}
			len++;
			start = 0;
		}
		//print(substrings);	
		set<string> consonantSubs;
		int runningCount = 0;
		for (int i = 0; i < word.size(); i++)
		{
			if (IsConsonant(word[i]))
			{
				runningCount++;
				if (runningCount == n)
				{
					string consonantSub = word.substr(i-n+1, n);
					consonantSubs.insert(consonantSub);
					runningCount--;
				}
			}
			else
			{
				runningCount = 0;
			}
		}
		//print(consonantSubs);
		int counter = 0;
		//set<int> *alreadySeen = new set<int>[n];
		for (set<string>::iterator it = consonantSubs.begin(); it != consonantSubs.end(); it++)
		{
			for (int j = 0; j < substrings.size(); j++)
			{
				if (substrings[j].substr.find(*it) != string::npos)
				{							   
					counter++;	
					substrings.erase(substrings.begin() + j);
					j--;
				}
			}
		}
		cout << "Case #" << caseNum << ": " << counter << endl;
	}
}

bool IsConsonant(char c)
{
	switch (c)
	{
	case 'a':
	case 'e':
	case 'i':
	case 'o':
	case 'u':
		return false;
	default:
		return true;
	}
}
