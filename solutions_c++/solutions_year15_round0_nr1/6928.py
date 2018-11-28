#include <iostream>

using namespace std;

int
main(void)
{
	int t = 0, tmp = 0;
	int clappingPeople = 0;
	int addedPeople = 0;
	int maxShiness = 0;
	string shiness;

	cin>>t;
	for (int index=0; index<t; index++)
	{
		clappingPeople = addedPeople = 0;
		cin >> maxShiness;
		cin >> shiness;
		clappingPeople += (int)(shiness[0]-'0');
		for (int i=1; i<maxShiness+1; i++)
		{
			if (clappingPeople < i)
			{
				tmp = i - clappingPeople;
				addedPeople += tmp;
				clappingPeople += tmp + (int)(shiness[i]-'0');
			}
			else
			{
				clappingPeople += (int)(shiness[i]-'0');
			}
		}
		cout << "Case #" << index + 1 << ": " << addedPeople << endl;
	}
	return 0;
}
