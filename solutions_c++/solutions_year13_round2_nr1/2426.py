#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

typedef int num;

int main()
{
	int numCases;
	cin >> numCases;
	for (int caseNum = 1; caseNum <= numCases; caseNum++)
	{
		num A;
		cin >> A;
		num N;
		cin >> N;
		vector<num> motes;
		for (num i = 0; i < N; i++)
		{
			num mote;
			cin >> mote;
			motes.push_back(mote);
		}
		sort(motes.begin(), motes.end());
		num counter = 0;
		while (motes.size() > 0)
		{
			vector<num>::iterator it;
			for (it = motes.begin(); it < motes.end(); it++)
			{
				if (*it < A)
				{
					A += *it;
				}
				else
				{
					break;
				}
			}
			if (it > motes.begin())
			{
				motes.erase(motes.begin(), it);
			}
			if (motes.size() == 0)
			{
				break;
			}
			num min = *motes.begin();
			num tempCounter = 0;
			while (A <= min)
			{			
				if (A-1 == 0)
					break;
				A += (A-1);
				tempCounter++;
			}
			if (tempCounter < motes.size() && tempCounter != 0)
			{
				counter += tempCounter;
			}
			else
			{				
				counter += motes.size();
				motes.clear();
			}
		}
		cout << "Case #" << caseNum << ": " << counter << endl;
	}
}
