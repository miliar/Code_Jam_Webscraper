#include <iostream>
#include <unordered_set>
#include <cstdio>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int la, lb;
		int t1[16], t2[16];
		cin >> la;
		for (int k = 0; k < 16; k++) cin >> t1[k];
		cin >> lb;
		for (int k = 0; k < 16; k++) cin >> t2[k];
		
		unordered_set<int> occur;
		for (int k = 0; k < 4; k++)
		{
			occur.insert(t1[(la - 1) * 4 + k]);
		}
		
		int total = 0, result;
		for (int k = 0; k < 4; k++)
		{
			if (occur.count(t2[(lb - 1) * 4 + k]) != 0)
			{
				total++;
				result = t2[(lb - 1) * 4 + k];
			}
		}
		
		if (total == 1)
		{
			printf("Case #%d: %d\n", t + 1, result);
		} else if (total > 1)
		{
			printf("Case #%d: Bad magician!\n", t + 1);
		} else {
			printf("Case #%d: Volunteer cheated!\n", t + 1);
		}
	}
	
	return 0;
}
