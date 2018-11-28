#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>

using namespace std;



int solver(vector<int> pancakes)
{
	sort(pancakes.rbegin(), pancakes.rend());
	int worst = pancakes[0];
	if(worst <= 2)
	{
		return worst;
	}

	int best = worst;
	for(int x=1; x<=(worst/2); x++)
	{
		vector<int> pancakesT(pancakes);
//		int half = (worst+1)/2;
		int half = worst - x;

		int curScore = 1;
		for(int i=1; i<pancakesT.size(); i++)
		{
			if(pancakesT[i] > half)
			{
				curScore++;
			}
		}

//		if((curScore + half) < best)
		if(1)
		{
			for(int i=0; i<curScore; i++)
			{
				int value = pancakesT[0];
				pancakesT.erase(pancakesT.begin());
				pancakesT.insert(pancakesT.end(), half);
				pancakesT.insert(pancakesT.end(), value-half);
			}
			int nextIter = solver(pancakesT);
			if(nextIter < half)
			{
				curScore += nextIter;
			}
			else
			{
				curScore += half;
			}
			best = min(best, curScore);
		}
	}
	return best;
}


int main()
{
	int tests;
	cin >> tests;

	for(int a=0; a<tests; a++)
	{
		int howMany;
		cin >> howMany;

		vector<int> pancakes(howMany, 0);
		for(int i=0; i<howMany; i++)
		{
			cin >> pancakes[i];
		}

		int retval = solver(pancakes);

		cout << "Case #" << (a+1) << ": " << retval << endl;;
	}

	return 0;
}
