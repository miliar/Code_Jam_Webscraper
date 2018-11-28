//////////////////////////////////////////////
//Author: Adrian Seitan: seitan.adi@gmail.com
//////////////////////////////////////////////

#include<bits/stdc++.h>

using namespace std;

bool foundStr(string sourceStr, string strToFind)
{
	for (int i = 0; i < sourceStr.size(); i++)
	{
		for (int j = 0; j < strToFind.size(); j++)
		{
			if (sourceStr[i] == strToFind[j])
			{
				sourceStr.at(i) = 'q';
				strToFind.at(j) = 'Q';
			}
		}
	}

	for (int j = 0; j < strToFind.size(); j++)
	{
		if (strToFind[j] != 'Q') return false;
	}
	return true;
}

void findAndReplaceStr(string &sourceStr, string &strToFind)
{
	for (int i = 0; i < sourceStr.size(); i++)
	{
		for (int j = 0; j < strToFind.size(); j++)
		{
			if (sourceStr[i] == strToFind[j])
			{
				sourceStr.at(i) = 'q';
				strToFind.at(j) = 'Q';
			}
		}
	}
}

bool stringToFind(string &sourceStr, string strToFind, string & result)
{
	if (foundStr(sourceStr, strToFind))
	{
		findAndReplaceStr(sourceStr, strToFind);
		return true;
	}
	else
	{
		return false;
	}
}

string parseTestCase(string pstr)
{
	string result;
	string numbs[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	vector<int> res;
	
	string pstr2 = pstr;

	bool repeatInverse = false;
	for (int i = 0; i < 10; i++)
	{
		bool repeat = true;
		while (repeat)
		{
			repeat = stringToFind(pstr2, numbs[i], result);
			if (repeat) res.push_back(i);
		}
	}

	for (int j = 0; j < pstr2.size(); j++)
	{
		if (pstr2[j] != 'q') {repeatInverse = true; break;}
	}

	if (repeatInverse)
	{
		res.clear();
		for (int i = 9; i >= 0; i--)
		{
			bool repeat = true;
			while (repeat)
			{
				repeat = stringToFind(pstr, numbs[i], result);
				if (repeat) res.push_back(i);
			}
		}
	}


	sort(res.begin(), res.end());
	for (int i = 0; i < res.size(); i++)
	{
		result += to_string(res[i]);
	}

	return result;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int cases, writtenCase = 1;
	cin >> cases;
	while (--cases >= 0)
	{
		string strLine;
		cin >> strLine;
		cout << "Case #" << writtenCase++ << ": " << parseTestCase(strLine) << endl;
	}

	return 1;
}

