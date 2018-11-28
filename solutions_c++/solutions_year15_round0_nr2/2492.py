#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

bool myfunction(int i, int j) { return (i>j); }

int check_cost(vector <int> &stacks, int number_of_people)
{
	sort(stacks.begin(), stacks.end(), myfunction);
	int cost = stacks[0] / 2;

	if (stacks[0] <= 3)
	{
		cost = -1;
	}
	else if (number_of_people == 1)
	{

	}
	else
	{
		for (int i = 1; i < number_of_people; i++)
		{
			if (stacks[0] > stacks[i] + 1)
			{
				break;
			}
			else
			{
				cost--;
			}
		}
	}
	return cost;
}

int main()
{
	int cases;
	int current_case = 0;
	vector<int> stacks;
	cin >> cases;
	while (cases)
	{
		stacks.clear();
		cases--;
		current_case++;
		int time = 0;
		int number_of_people = 0;
		int cost = 0;
		cin >> number_of_people;
		for (int i = 0; i < number_of_people; i++)
		{
			int temp;
			cin >> temp;
			stacks.push_back(temp);
		}
		// time cannot exceeed 9
		time = *max_element(stacks.begin(), stacks.end());
		int eating_time = 2;
		while (eating_time < time)
		{ 
			int temp_total = 0;
			for (int i = 0; i < stacks.size(); i++)
			{
				temp_total += ((stacks[i] - 1) / (eating_time));
			}
			temp_total += eating_time;
			time = min(time, temp_total);
			eating_time++;
		}
		printf("Case #%d: %d\n", current_case, time);
		
		
	}
 }