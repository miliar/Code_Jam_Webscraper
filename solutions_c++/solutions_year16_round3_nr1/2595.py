// TestProgram.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

class CalculateEvaucationPlan
{
	vector<int> elements;
	int number_of_parties = 0;
	int number_of_senators = 0;
	int first_index = 0;
	int second_index = 0;
	int first = 0;
	int second = 0;
	int done = 0;
	int not_null_num = 0;
	vector<int>::iterator it;
	int index = 0;

	void ReadSenators()
	{
		cin >> number_of_parties;  // read n and then m.
		for (int j = 0; j < number_of_parties; ++j)
		{
			int act;
			cin >> act;
			elements.push_back(act);
			number_of_senators += act;
		}

	}

	void FindFirstTwoElement()
	{
		first = first_index = second = second_index = index = not_null_num = 0;
		for (it = elements.begin(); it != elements.end(); ++it)
		{
			if (first <= (*it))
			{
				second_index = first_index;
				second = first;
				first_index = index;
				first = *it;
			}
			else if(second <= (*it))
			{
				second_index = index;
				second = *it;
			}
			if (*it)
				not_null_num++;
			index++;
		}
	}

	void EvacuationIterStep()
	{
		if (first == second)
		{
			if (first > 1)
			{
				cout << (char)('A' + first_index) << (char)('A' + second_index) << " ";
				elements[first_index]--;
				elements[second_index]--;
				done += 2;
			}
			else
			{
				if (!(not_null_num % 2))
				{
					cout << (char)('A' + first_index) << (char)('A' + second_index) << " ";
					elements[first_index]--;
					elements[second_index]--;
					done += 2;
				}
				else
				{
					cout << (char)('A' + first_index) << " ";
					elements[first_index]--;
					done++;
				}
			}
		}
		else
		{
			if (first > 2)
			{
				cout << (char)('A' + first_index) << (char)('A' + first_index) << " ";
				elements[first_index]--;
				elements[first_index]--;
				done += 2;
			}
			else
			{
				cout << (char)('A' + first_index) << " ";
				elements[first_index]--;
				done++;
			}
		}
	}

public:
	void Calculate()
	{
		ReadSenators();
		while (done != number_of_senators)
		{
			FindFirstTwoElement();
			EvacuationIterStep();
		}
	}
};

/*void CalculateEvaucationPlan(vector<int> & elements)
{
	int first_index = 0;
	int second_index = 0;
	int first = 0;
	int second = 0;
	int done = 0;
	int not_null_num = 0;
	vector<int>::iterator it;
	int index = 0;
	for (it = elements.begin(); it != elements.end(); ++it)
	{
		if(first <= (*it))
		{
			second_index = first_index;
			second = first;
			first_index = index;
			first = (*it);
		}
		if (*it)
			not_null_num++;
		index++;
	}
	if(first == second)
	{
		if(first > 1)
		{
			cout << first_index << second_index << " ";
			elements[first_index]--;
			elements[second_index]--;
			done += 2;
		}
		else
		{
			if(not_null_num % 2)
			{
				cout << first_index << second_index << " ";
				elements[first_index]--;
				elements[second_index]--;
				done += 2;
			}
			else
			{
				cout << first_index << " ";
				elements[first_index]--;
				done++;
			}
		}
	}
	else
	{
		if(first > 2)
		{
			cout << first_index << first_index << " ";
			elements[first_index]--;
			elements[first_index]--;
			done += 2;
		}
		else
		{
			cout << first_index << " ";
			elements[first_index]--;
			done++;
		}
	}
}*/

void main() {
	int t, n;
	vector<int> elements;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		CalculateEvaucationPlan evacuationPlan;
		evacuationPlan.Calculate();
		cout << endl;
	}
}

