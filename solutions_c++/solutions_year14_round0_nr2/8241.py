#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int testCases;
	int id =1;
	double farmCost, farmImprove, win;

	cin>>testCases;
	
	while(testCases--)
	{
		cin>>farmCost>>farmImprove>>win;
		double time = 0;
		double cookie = 0;
		double add = 2;

		while(true)
		{
			cookie += add;

			if(cookie >= farmCost)
			{
				cookie = farmCost;
				if((win - cookie)/add > (win)/(add+farmImprove))
				{

					cookie = 0;
					time += farmCost/add;
					//cout<<farmCost/add<<endl;
					add += farmImprove;
					//cout<<time<<endl;

				}
				else
				{
					//cout<<(win)/add<<endl;
					time += (win)/add;
					break;
				}	
			}

		}

		cout<<"Case #"<<id++<<": "<<fixed<<setprecision(7)<<time<<endl;


	}	


	return 0;
}	
