#include <stdio.h>
#include <vector>
#include <iostream>    
#include <algorithm>


using namespace std;


int main()
{
	vector<double> Naomi;  
	vector<double> Ken;
	double block;
	int l,t,i,b,Ni,Nj,Kj,Ki,war,dwar;  

	scanf("%d", &t);

	for(l=0; l<t; l++)
	{
		scanf("%d", &b);
		for(i=0; i<b; i++)
		{
			scanf("%lf", &block);
			Naomi.push_back(block);
		}
		for(i=0; i<b; i++)
		{
			scanf("%lf", &block);
			Ken.push_back(block);
		}
		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());
		Ni = 0; Ki = 0;
		Nj = b-1; Kj = b-1;
		war = 0; dwar = 0;
		for(i=0; i<b; i++)
		{

			if(Naomi[Nj] > Ken[Kj])
			{
				//printf("%lf > %lf\n", Naomi[Nj] , Ken[Kj]);
				war++;	
				Nj--;
			}
			else
			{
				Kj--; Nj--;
			}
		}

		Ni = 0; Ki = 0;
		Nj = b-1; Kj = b-1;
		for(i=0; i<b; i++)
		{
			if(Naomi[Ni] < Ken[Ki])
			{
				Ni++;
				Kj--;
			}
			else
			{
				Ni++;
				Ki++;
				dwar++;
			}
		}

		printf("Case #%d: %d %d\n", l+1, dwar, war);

		Naomi.clear();
		Ken.clear();

	}
	return 0;
}