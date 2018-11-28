#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

int main()
{
	ifstream f;
	f.open("standing-ovation.in");
	int t, smax;
	string people;
	f >> t;
	for (int k = 1; k <= t; k++)
	{
		f >> smax >> people;
		int needed = 0;
		int standing = 0;
		for (int j = 0; j < smax + 1; j++)
		{
			if (standing < j)
			{
				int curr = j - standing;
				needed += curr;
				standing += curr;
			}
			standing += people[j] - '0';
		}
		printf("Case #%d: %d\n", k, needed);
	}
}
