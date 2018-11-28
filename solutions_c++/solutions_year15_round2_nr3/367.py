#include <iostream>
#include <algorithm>
using namespace std;
#define int long long
pair<int, int> czas[5];
main()
{
	int ilez;
	cin>>ilez;
	for(int aa=0; aa<ilez; aa++)
	{
		int ilegrup;
		cin>>ilegrup;
		int ilewszystkich=0;
		for(int i=0; i<ilegrup; i++)
		{
			int ilewgrupie;
			int start, najszybszy;
			cin>>start>>ilewgrupie>>najszybszy;
			for(int a=0; a<ilewgrupie; a++)
			{
				czas[ilewszystkich].first=(najszybszy+a)*(360-start);
				czas[ilewszystkich].second=czas[ilewszystkich].first+(najszybszy+a)*360;
				ilewszystkich++;
			}

		}
		if(ilewszystkich<2)
		{
			cout<<"Case #"<<aa+1<<": 0"<<endl;
			continue;
		}
		sort(czas, czas+ilewszystkich);
		if(czas[0].second<=czas[1].first)
		{
			cout<<"Case #"<<aa+1<<": 1"<<endl;
		}
		else
		{
			cout<<"Case #"<<aa+1<<": 0"<<endl;
		}
	}
}
