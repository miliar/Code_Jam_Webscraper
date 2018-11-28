#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <limits.h>
#include <bitset>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

int t;


void print(vector<int> set)
{
	for(int i=0; i < set.size(); i++)
	{
		cout << set.at(i) << ", ";
	}
	cout << endl;
}

	
bool valid(vector<int> set)
{
	for(int i=0; i < set.size(); i++)
	{
		if(set.at(i)==0)
		{
			return false;
		}
	}
	return true;
}

void change(vector<char> *set)
{
	int size = set->size();
	int count = 0;

	/*
	if(ss.at(i)!=ss.at(i-1))
	{
		cout << "at " << (i-1) << " and " << (i) << endl;
		reverse(ss.begin(), ss.begin()+(i-1));

			
		for(int j=0; j <= (i-1); j++)
		{
			if(ss.at(j)=='-')
			{
				ss.at(j) = '+';
			}
			else if(ss.at(j)=='+')
			{
				ss.at(j) = '-';
			}
		}
			
			
		print(ss);
		count += 1;
	}
	*/
}

int compute(vector<int> set)
{
	int countswaps = 0;
	int position = 0;
	while(true)
	{
		if(valid(set))
		{
			return countswaps;
		}

		int swapto = 0;
		for(int i=1; i < set.size(); i++)
		{
			if(set.at(i)==set.at(i-1))
			{
				swapto +=1;
			}
			else
			{
				break;
			}
		}

		reverse(set.begin(), set.begin()+swapto);
		for(int i=0; i <= swapto; i++)
		{
			if(set.at(i)==0)
			{
				set.at(i) = 1;
			}
			else if(set.at(i)==1)
			{
				set.at(i) = 0;
			}
		}

		countswaps += 1;
	}
}


int main()
{
	cin >> t;
	for(int tt=0; tt < t; tt++)
	{
		string ss;
		getline(cin, ss);
		if(ss.length()<=0)
		{
			getline(cin, ss);
		}
		
		vector<int> set;
		for(int i=0; i < ss.length(); i++)
		{
			if(ss.at(i)=='-')
			{
				set.push_back(0);
			}
			else
			{
				set.push_back(1);
			}
		}		
		cout << "Case #" << (tt+1) << ": " << compute(set) << endl;
	}
	
	
	return 0;
}
