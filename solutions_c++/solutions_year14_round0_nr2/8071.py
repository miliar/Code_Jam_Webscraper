#include <iostream>
#include <fstream>
#include <iomanip>

#define sfi(x) scanf("%d",&x);
#define sfd(x) scanf("%lf",&x);

using namespace std;

int main()
{
	
	freopen("B-large.in","r",stdin);
	freopen("outputy.txt","w",stdout);

	int T;
	
	double requiredcc;
	double cost_of_farm;
	double rate_of_farm;

	double ans;
	double speed;

	sfi(T);

	for(int t=1;t<=T;t++)
	{

		sfd(cost_of_farm);
		sfd(rate_of_farm);
		sfd(requiredcc);

		ans = 0;

		if(requiredcc < rate_of_farm)
		{
			ans = requiredcc/2;
		}


		else
		{
			speed = 2;

			while(1)
			{

				ans += (cost_of_farm/speed);

				if(((requiredcc-cost_of_farm)/speed) < (requiredcc/(speed + rate_of_farm)))
				{
					ans += (requiredcc-cost_of_farm)/speed;
					break;
				}

				speed = speed + rate_of_farm;

			}
		}

			
		printf("Case #%d: %.7lf\n",t,ans);

	}
}