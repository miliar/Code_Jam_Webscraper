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


int main()
{
	string storage;
	int cases;
	int current_case = 1;
	cin >> cases;
	while (cases)
	{
		int people_needed = 0;
		int number = 0;
		int current_number = 0;
		int total = 0;
		int current_shy = 0;
		char it;
		cases--;
		int Shy_max;
		cin >> Shy_max;
		getline(cin, storage);

		for (int i = 0; i < Shy_max + 1; i++)
		{
			it = storage[i+1];
			//current number of shyness
			current_number = atoi(&it);
			while (total < current_shy)
			{
				people_needed++;
				total++;
			}
			total += current_number;
			current_shy++;
			it++;
		}
		printf("Case #%d: %d\n",current_case,people_needed);
		current_case++;
	}
}