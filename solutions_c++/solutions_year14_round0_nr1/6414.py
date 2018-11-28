#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include<iostream>
#include<vector>

using namespace std;
int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int testCases;

	cin>>testCases;

	for (int x = 1; x <= testCases; x++)
	{
		int rowOne;
		cin>>rowOne;

		vector<int> rowArray;
		for (int i = 0; i < 4; i++)
		{
			for (int j= 0; j < 4; j++)
			{
				int temp;
				cin>>temp;
				if (i == rowOne-1)
				{
					rowArray.push_back(temp);
				}
			}
		}

		int rowTwo;
		cin>>rowTwo;

		vector<int> rowArrayTwo;
		for (int i = 0; i < 4; i++)
		{
			for (int j= 0; j < 4; j++)
			{
				int temp;
				cin>>temp;
				if (i == rowTwo-1)
				{
					rowArrayTwo.push_back(temp);
				}
			}
		}

		vector<int>::const_iterator locationOut;
		int counter = 0;
		for (int i = 0; i < 4; i++)
		{
			int value= rowArray[i];

			// Find the first element in the range [first, last)
			// that matches value.
			vector<int>::const_iterator location = find(rowArrayTwo.begin(), rowArrayTwo.end(), value);

			if (location != rowArrayTwo.end())         // matching element found
			{
				counter++;
				locationOut = location;
			}
		}

		/*
		Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!
		*/

		if (counter == 0)
		{
			cout<<"Case #"<<x<<": "<<"Volunteer cheated!"<<endl; 
		}
		else if (counter > 1)
		{
			cout<<"Case #"<<x<<": "<<"Bad magician!"<<endl; 
		}
		else
		{
			//int ans = rowArrayTwo[location - rowArrayTwo.begin()];
			cout<<"Case #"<<x<<": "<<*locationOut<<endl; 
		}


	}

	return 0;
}