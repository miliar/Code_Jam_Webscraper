#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stack>
#include <math.h>
#include <algorithm>
//#include <pair>
#include <hash_set>
#include <set>

using namespace std;
using namespace stdext;

bool openFileHandles(ifstream& readFile, const string& inFile, ofstream& writeFile, const string& outFile);

namespace
{
	typedef long long ll;
	typedef pair<ll, ll> pll;
	const ll MAX = ll(2e18);
}


int main()
{
	// files
	ifstream readFile;
	ofstream writeFile;

	string fileIn = //"practice";
					"small";
					//"large";

	if (!openFileHandles(readFile, fileIn + ".in", writeFile, fileIn + ".out"))
		return -1;

	// read # of lines
	int T;
	readFile >> T;
	readFile.get();  // get rid of the newline

	//char vowels[] = {'a', 'e', 'i', 'o', 'u'};
	stdext::hash_set<char> vowels;
	vowels.insert('a');
	vowels.insert('e');
	vowels.insert('i');
	vowels.insert('o');
	vowels.insert('u');

	// for each test case, ... 
	for (int t = 1; t <= T; ++t)
	{
		// 1. read in file
		string name; int n;
		readFile >> name >> n; readFile.get();
		
		std::set<pair<int, string> > words;
		for (int i = 0; i < name.size(); ++i)
		{
			for (int j = i; j < name.size(); ++j)
			{
				string curr = name.substr(i, name.size()-j);
				//cout << curr << endl;

				int count = 0;
				for (int k = 0; k < curr.size(); ++k)
				{
					if (vowels.find(curr[k]) == vowels.end())
						++count;
					else
						count = 0;

					if (count == n &&
						words.find(pair<int, string>(i, curr)) == words.end())
					{
						count = 0;
						words.insert(pair<int, string>(i, curr));
						break;
					}
				}
			}
		}

		//cout << "Case #" << t << ": " << words.size() << endl;
		writeFile << "Case #" << t << ": " << words.size() << endl;

	}  // for (t)

	// close file handles
	readFile.close();
	writeFile.close();

	// no error
	return 0;
}

bool openFileHandles(ifstream& readFile, const string& inFile, ofstream& writeFile, const string& outFile)
{
	// input file
	readFile.open(inFile.c_str());
	if (!readFile)
	{
		cout << "Could not find '" << inFile << "'\n\n";
		return false;
	}

	// output file
	writeFile.open(outFile.c_str());
	if (!writeFile)
	{
		cout << "Could not find '" << outFile << "'\n\n";
		return false;
	}

	return true;
}
