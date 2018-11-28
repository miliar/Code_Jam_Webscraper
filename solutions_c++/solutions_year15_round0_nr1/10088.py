#include <string>
#include <vector>
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	unsigned cases=0;
	unsigned order=1;
	cin >> cases;
	//cout << "Num of cases: "<<cases<<endl;
	while(cases)
	{
		unsigned smax=0;
		cin >> smax;
		getchar();
		vector<int> s(smax+1,0);
		for(int i=0;i<=smax;i++)
			s[i] = getchar()-'0';
		/*for(int i=0;i<=smax;i++)
			cout << s[i]<<", ";
		cout<<endl;*/

		int numPeople=s[0];
		int ans=0;
		for(int i=1;i<=smax;i++)
		{
			if(s[i])
			{
				if(numPeople<i)
				{
					ans+=i-numPeople;
					numPeople+=ans;
				}	
				numPeople+=s[i];
			}
		}
		cout<<"Case #"<<order<<": "<<ans<<endl;

		order++;
		cases--;
	}
	return 0;
}