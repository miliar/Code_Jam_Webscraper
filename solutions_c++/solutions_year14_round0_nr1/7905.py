#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

void printset(set<int> s)
{
	for (set<int>::iterator it = s.begin(); it != s.end(); it++)
	{
		cout << *it << " ";
	}
	cout << endl;
}

int main()
{
	int numCases;
	cin >> numCases;
	for (int caseNum = 1; caseNum <= numCases; caseNum++)
	{
		int row1, row2;
		int temp;
		set<int> first, second;
		vector<int> intersection(4);
		vector<int>::iterator it;
		cin >> row1;
		for (int j = 0; j < 16; j++)
		{
			cin >> temp;
			if (j >= 4*row1-4 && j < 4*row1)
			{
				first.insert(temp);
			}		 
		}
		cin >> row2;
		for (int j = 0; j < 16; j++)
		{
			cin >> temp;
			if (j >= 4*row2-4 && j < 4*row2)
			{
				second.insert(temp);
			}
		}
		//printset(first);
		//printset(second);
		it = set_intersection(first.begin(), first.end(), second.begin(), second.end(), intersection.begin());
		intersection.resize(it - intersection.begin());
		if (intersection.size() == 1)
		{
			cout << "Case #" << caseNum << ": " << intersection[0] << endl;
		}
		else if (intersection.size() > 1)
		{
			cout << "Case #" << caseNum << ": Bad magician!" << endl;
		}
		else if (intersection.empty())
		{
			cout << "Case #" << caseNum << ": Volunteer cheated!" << endl;
		}
	}
}
