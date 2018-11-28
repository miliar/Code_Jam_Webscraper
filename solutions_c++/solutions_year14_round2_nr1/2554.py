#include <iostream>
#include <vector>
#include <limits>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iomanip> 
#include <fstream> 
#include <sstream>
#include <stack>
#include <string.h>

using namespace std;

bool allEmpty(vector<string>& words)
{
	for(int i = 0; i < words.size(); i++)
		if(words[i] != "")
			return false;
	return true;
}

void removeFirst(vector<string>& words)
{
	for(int i = 0; i < words.size(); i++)
	{
		words[i] = words[i].substr(1);
	}
}

bool allSame(vector<string>& words, int i)
{
	if(words.size() == 0)
		return true;
	for(int k = 1; k < words.size(); k++)
		if(words[k].length() == 0 || words[0].length() == 0 || words[k][i] != words[0][i])
			return false;
	return true;
}

int main()
{
	ifstream ifs = ifstream("C:\\Users\\Mike\\Documents\\a.in");
	ofstream ofs = ofstream("C:\\Users\\Mike\\Documents\\a.out");

	int t;
	ifs >> t >> ws;

	for(int g = 0; g < t; g++)
	{
		int n;
		ifs >> n;
		vector<string> words(n);
		for(int i = 0; i < n; i++)
			ifs >> words[i];
		bool good = true;
		int count = 0;
		while(!allEmpty(words) && good)
		{
			if(allSame(words, 0))
			{
				vector<int> counts(words.size());
				for(int i = 0; i < words.size(); i++)
				{
					counts[i] = 0;
					while(words[i].length() > 1 && words[i][0] == words[i][1])
					{
						counts[i]++;
						words[i] = words[i].substr(1);
					}
				}
				double average = 0;
				for(int i = 0; i < counts.size(); i++)
					average += counts[i];
				average /= counts.size();
				int iav = (int)(average + 0.5);
				for(int i = 0; i < counts.size(); i++)
					count += abs(counts[i] - iav);
				removeFirst(words);
			}
			else
			{
				good = false;
			}
		}
		ofs << "Case #" << (g + 1) << ": ";
		if(good)
			ofs << count << endl;
		else
			ofs << "Fegla won" << endl;
	}

	//cin.get();cin.get();
	return 0;
}