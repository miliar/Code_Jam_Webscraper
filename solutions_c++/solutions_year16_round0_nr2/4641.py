#include "fstream"
#include "vector"
#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
using namespace std;

int GetIndex(vector<int> v)
{
	int p = 0;

	

	if (p == v.size())
		return -1;

	int i = v.size() - 1;
	for (; i >= 0 && v[i] == 1; i--);
	
	if (v[0] == -1)
		return i;
	else
	{
		int j = i;
		for (; j > 0 && v[j] == -1; j--);
		return j;
	}
	

}

int main()
{

	ifstream inputFile;
	inputFile.open("B-large.in");
	//inputFile.open("Test.txt");
	ofstream outputFile;
	outputFile.open("result");
	vector<int> myMap;
	int T;
	inputFile >> T;
	string s;
	getline(inputFile, s);
	vector<int> v;
	for (int t = 1; t <= T; t++)
	{

		getline(inputFile, s);
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '-')
				v.push_back(-1);
			else
				v.push_back(1);
		}

		int c = 0;
		for (; c < v.size(); c++)
		{
			int idx = GetIndex(v);

			if (idx == -1)
				break;

			int i = 0;
			int j = idx;
			for (; i <= j; i++)
			{
				int tmp = v[i];
				v[i] = -1 * v[j];
				v[j] = -1 * tmp;
				j--;
			}
		}

		cout << "Case #" << t << ": " << c << endl;
		outputFile << "Case #" << t << ": " << c << endl;
		 
		v.clear();
	}
	return 0;
}
