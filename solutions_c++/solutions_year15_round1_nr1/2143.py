#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int max(int a, int b)
{
	return (a > b) ? a : b;
}
int min(int a, int b)
{
	return (a < b) ? a : b;
}
void eatMushroom(int numMushroom[],int n,int j)
{
	ofstream output;
	output.open("A-large.out", ios::app);
	int x = 0;
	int y = 0;
	for (int i = 0; i < n - 1; i++)
	{
		if (numMushroom[i] >= numMushroom[i + 1])
			x += numMushroom[i] - numMushroom[i + 1];
	}
	int maxSub = 0;
	bool flag = false;
	for (int i = 0; i < n - 1; i++)
	{
		if (numMushroom[i] - numMushroom[i + 1] >= 0)
			flag = true;
		maxSub = max(maxSub, numMushroom[i] - numMushroom[i + 1]);
	}
	for (int i = 0; i < n - 1; i++)
	{
		if (numMushroom[i] <= maxSub)
			y += numMushroom[i];
		else
			y += maxSub;
	}
	output << "Case #" << j+1 << ": " << x << " " << y << endl;
	output.close();
}
int main()
{
	int t = 0;
	ifstream input;
	

	input.open("A-large.in");
	
	input >> t;
	for (int i = 0; i < t; i++)
	{
		int n = 0;
		input >> n;
		int *numMushroom = new int[n];
		for (int j = 0; j < n; j++)
		{
			input >> numMushroom[j];
		}
		eatMushroom(numMushroom, n, i);
	}
	input.close();
	return 0;
}