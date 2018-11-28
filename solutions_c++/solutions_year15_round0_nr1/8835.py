#define _WINSOCK_DEPRECATED_NO_WARNINGS
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <random>
#include <fstream>
#include <array>

using namespace std;

int main()
{
	fstream fin("in.in");
	fstream fout("out.txt");
	int testcase;
	fin >> testcase;
	for (int i = 0; i < testcase; i++)
	{
		int Smax;
		fin >> Smax;
		string s; 
		fin >> s;
		int peopleCount = 0, frndCount = 0;
		for (int i = 0; i <= Smax; i++)
		{
			if (peopleCount >= i)
				peopleCount += (s[i] - 48);
			else
			{
				frndCount += (i - peopleCount);
				peopleCount = i + (s[i] - 48);
			}
		}
		fout << "Case #" << i + 1 << ": " << frndCount << endl;
	}
}
/*void route(int adjacenyMatrix[][17])
{
	int connectedPath[17][17] = { 0 };
	cout << "Enter the number of routings you wish to perform" << endl;
	int route;
	cin >> route;
	for (int i = 0; i < route; i++)
	{
		int source, dest;
		cout << "Enter Source and Dest" << endl;
		cin >> source >> dest;


		int distance[17];
		fill(distance, &distance[17], INT_MAX);
		distance[source - 1] = 0;

		vector<int> shortestPathSet;
		while (shortestPathSet.size() < 17)
		{
			int min = INT_MAX - 1;
			int position = -1;
			for (int i = 0; i < 17; i++)
				if (!contains(shortestPathSet, i) && distance[i] <= min)
				{
					position = i;
					min = distance[i];
				}
			if (position == -1)
				break;
			shortestPathSet.push_back(position);
			for (int i = 0; i < 17; i++)
			{
				if (adjacenyMatrix[position][i] != 0 && !contains(shortestPathSet, i))
					if (distance[position] + adjacenyMatrix[position][i] < distance[i])
					{
						distance[i] = distance[position] + adjacenyMatrix[position][i];
						connectedPath[position][i] = 1;
					}
			}
		}
		for (int i = 0; i < 17; i++)
		{
			for (int j = 0; j < 17; j++)
				cout << adjacenyMatrix[i][j] << " ";
			cout << endl;
		}
		if (distance[dest - 1] == INT_MAX)
			cout << "No Route Possible" << endl;
		else
			cout << "Speed is " << distance[dest - 1] << endl;
	}
}

int main()
{
	int adjacenyMatrix[17][17] = { 0 };
	cout << "Enter the no. of paths" << endl;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cout << "Node A ---> Node B" << endl;
		cout << "Enter A and B" << endl;
		int a, b;
		cin >> a >> b;
		if (a <= 0 || b <= 0 || a >= 18 || b >= 18)
		{
			cout << "Re-Enter" << endl;
			i--;
			continue;
		}
		adjacenyMatrix[a - 1][b - 1] = 1;
	}
	for (int i = 0; i < 17; i++)
		for (int j = 0; j < 17; j++)
		{
			int randomNo = rand() % 9 + 1;
			adjacenyMatrix[i][j] *= randomNo;
		}
	route(adjacenyMatrix);

	cout << "How many edges you want to delete?" << endl;
	int edgeDelete;
	cin >> edgeDelete;
	for (int i = 0; i < edgeDelete; i++)
	{
		cout << "Node A ---> Node B" << endl;
		cout << "Enter A and B" << endl;
		int a, b;
		cin >> a >> b;
		if (a <= 0 || b <= 0 || a >= 18 || b >= 18)
		{
			cout << "Re-Enter" << endl;
			i--;
			continue;
		}
		adjacenyMatrix[a - 1][b - 1] = 0;
	}
	route(adjacenyMatrix);

	cin >> n;
}*/