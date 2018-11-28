#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int tcases;
	cin >> tcases;
	for ( int cas = 1; cas <= tcases; cas++)
	{
		int a, n, temp;
		vector<int> mote;
		cin >> a >> n;
		for ( int i = 0; i < n; i++)
		{
			cin >> temp;
			mote.push_back(temp);
		}
		if( a == 1)
		{
			cout << "Case #" << cas << ": " << n << "\n";
			continue;
		}
		sort ( mote.begin(), mote.end());
		vector <int> culmote;
		culmote.push_back(a);
		int cost = 0;
		for( int i = 0; i < mote.size(); i++)
		{
			if( mote[i] < culmote[i])
				culmote.push_back( mote[i] + culmote[i]);
			else
			{
				int temp = culmote[i], tempcost = 0;
				while( temp <= mote[i])
				{
					temp = 2 * temp - 1;
					tempcost++;
				}
				if( tempcost < mote.size() - i)
				{
					cost += tempcost;
					culmote.push_back( temp + mote[i]);
				}
				else
				{
					cost += mote.size() - i;
					break;
				}
			}
		}
		cout << "Case #" << cas << ": " << cost << "\n";
	}
}