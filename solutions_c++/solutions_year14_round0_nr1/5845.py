#include <cstdio>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int T;


vector<int> v1, v2;

void do_case(int num) 
{
	int row;
	cin >> row;
	v1.clear();
	v2.clear();
	for (int i = 1; i < 5; ++i) 
	{
		for (int j = 0; j < 4; ++j)
		{
			int n;
			cin >> n;
			if (row == i) 
			{
				v1.push_back(n);
			}
		}
	}

	cin >> row;
	for (int i = 1; i < 5; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			int n;
			cin >> n;
			if (row == i)
			{
				v2.push_back(n);
			}
		}
	}

	int count = 0;
	int number = 0;
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
		{
			if (v1[i] == v2[j])
			{
				count++;
				number = v1[i];
				break;
			}
		}

	printf("Case #%d: ", num+1);
	if (count == 1) 
	{
		printf("%d\n", number);
	}
	else if (count > 1)
	{
		printf("Bad magician!\n");
	}
	else {
		printf("Volunteer cheated!\n");
	}
}

int main() 
{
	cin >> T;
	for (int i = 0; i < T; ++i) 
	{
		do_case(i);
	}

	return 0;
}