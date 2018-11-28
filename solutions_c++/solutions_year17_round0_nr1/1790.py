#include <iostream>
#include <string>
#include <vector>

using namespace std;

int minimumFlip(vector<bool> &panList, int range)
{
	int currentPos = 0;
	int flipCount = 0;
	int panLength = panList.size();

	while(true)
	{
		while(panList[currentPos] == true)
		{
		currentPos++;
		if(currentPos == panLength)
		return flipCount;
		}

		if(currentPos + range > panLength)
		return -1;

		for(int idxPan = currentPos; idxPan < currentPos + range; idxPan++)
		{
		panList[idxPan] = !panList[idxPan];
		}

		flipCount++;
	}

	return flipCount;
}

int main()
{
	int t, k, s;

	cin >> t;
	for(int idxCase = 0; idxCase < t; idxCase++)
	{
		vector<bool> panList;
		string pan;
		int length;
		int range;

		cin >> pan >> range;

		length = pan.size();

		for(int idxPan = 0; idxPan < length; idxPan++)
		{
			if(pan.c_str()[idxPan] == '+')
			panList.push_back(true);
			else
			panList.push_back(false);
		}
  
		int minFlipCount = minimumFlip(panList, range);
		if(minFlipCount >= 0)
			cout << "Case #" << idxCase + 1 << ": " << minFlipCount << endl;
		else
			cout << "Case #" << idxCase + 1 << ": " << "IMPOSSIBLE" << endl;
	}

	return 0;
}
