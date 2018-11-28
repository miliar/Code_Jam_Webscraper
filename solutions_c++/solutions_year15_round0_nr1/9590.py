#include <iostream>
#include <vector>
#include <stdio.h>
#include <fstream>
#include <stdlib.h>

using namespace std;

int findFriends(string numShy)
{
	int friends = 0;
	unsigned int temp = 0;
	for (unsigned i = 0; i < numShy.size();)
	{	
		for (unsigned j = 0; j <= i; j++)
		{
			temp += numShy.at(j) - '0';
		}
		temp += friends;
		if (temp == i)
		{
			friends++;
			temp++;
		}
		i = temp;
		temp = 0;
	}

	return friends;
}

int main()
{
	int numCases = 0, maxShy = 0;
	cin >> numCases;
	vector <int> cases;	
	string numShy;
	ofstream outFile("output1.txt");
	if (!outFile)
	{
		exit(1);
	}

	for (int i = 0; i < numCases; i++)
	{
		cin >> maxShy;
		cin >> numShy;	
		cases.push_back(findFriends(numShy));
	}
	for (unsigned int i = 0; i < cases.size(); i++)
	{
		outFile << "Case #" << i+1 << ": " << cases.at(i) << endl;
	}	

	return 0;
}
