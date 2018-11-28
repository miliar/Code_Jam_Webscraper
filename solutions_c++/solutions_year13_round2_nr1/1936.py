#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <sstream>
#include <math.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;
int eat(unsigned long long &me, int other);
int solveMotes(unsigned long long size, int amount);

int main (void)
{
	string line;
	getline(cin,line);
	
	int cases = atoi(line.c_str()); // First line
	for (int i = 0; i < cases; i++)
	{
		unsigned long long size;
		cin >> size;
		int amount;
		cin >> amount;

		unsigned long long result = solveMotes(size, amount);

		cout << "Case #" << i+1 << ": " << result << endl;
	}	

	return 0;
}

int solveMotes(unsigned long long size, int amount)
{
	vector<int> motes(amount);
	for (int i = 0; i < amount; i++)
		cin >> motes[i];

	std::sort (motes.begin(), motes.end());

	int forward, mixed;
	forward = mixed = 0;
	int leastFor = 0;
	int leastMixed = 0;
	int hardDel = 0;

	for (int i = 0; i < amount; i++)
	{	
		if (motes[i] < size)
			size = size  + motes[i];
		else
		{	
			unsigned long long oldSize = size;
			if ((size == 1) && (motes[i] >= size))
			{	hardDel++;
				continue;
			}

			if (leastMixed == 0)
				leastMixed = 10000;

			mixed = forward + (amount - i);
			
			forward = forward + eat(size,motes[i]);//ceil(((double)motes[i]-size) / ((double)size-1));
			
			if (mixed != 0)
				if (mixed < leastMixed)
					leastMixed = mixed;

			leastFor += eat(oldSize,motes[i]);
		}
	//cout << "size " << size << " mote " << motes[i] << " mix " << mixed << " forward " << forward << " leastf " << leastFor << " leastm " << leastMixed << endl;
	}

	return min(leastFor,leastMixed)+hardDel;			
}

int eat(unsigned long long &me, int other)
{
	int res = 0;
	while (other >= me)
	{
		me += me-1;
		res++;
	}
	me = me + other;
	return res;
}

