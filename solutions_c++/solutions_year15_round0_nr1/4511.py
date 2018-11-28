#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef long long ll;

int main()
{
	ll casses;
	string others;
	cin >> casses;
	int totalStand;
	int extraPeople;
	int maxShy;
	for( int i = 0; i < casses && cin >> maxShy; i++ )
	{
		cerr << "new case " << endl;
		cin.ignore();
		cin >> others;
		totalStand = 0;
		//cout << others << endl;
		totalStand = (int)(others.at(0) - '0');
		extraPeople = 0;
		for(ll j = 1; j <= maxShy; j++ )
		{
			if( totalStand >= j || (int)(others.at(j) - '0') < 1 )
			{
				totalStand += (int)(others.at(j) - '0');
			}else
			{
				cerr << j << "  " << totalStand << endl;
				//cout << j << totalStand << endl;
				extraPeople += j - totalStand;
				totalStand += (int)(others.at(j) - '0') + extraPeople;
			}
		}
		//Case #1:
		cout << "Case #" << i + 1 << ": " << extraPeople << endl;
	}
	return 0;
}
