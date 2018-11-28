
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <tuple>

using namespace std;


#define ASSERT(X) {if (!(X)) {printf("\n assertion failed at line %d\n",__LINE__);exit(0);}}

double farm(int nbFarm, double c, double f, double lastAnswer)
{
	if (nbFarm <= 0)
	{
		return 0;
	}
	else
	{
		return (c / (2.0 + ((nbFarm - 1) * f))) + lastAnswer;
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		double c; //Prix d'une ferme
		double f; //Taux supplémentaire lors de l'achat d'une ferme
		double x; //Nb de cookies à avoir
		double time = 0;
		double res = 0;

		printf("Case #%d: ",case_id);
		scanf("%lf %lf %lf",&c,&f,&x);
		
		double currentRate = 2;
		int nbFarms = 0;

		while (1)
		{
			time = farm(nbFarms, c, f, time);
			double rate = (2.0 + (nbFarms * f));
			double newRes = time + (x / rate);
			if (res == 0)
			{
				res = newRes;
			}
			else
			{ 
				double newRes = time + (x / rate);
				if (newRes < res)
				{
					res = newRes;					
				}
				else
				{
					break;
				}
			}

			nbFarms++;
		}
		
		printf("%lf7\n", res);

		fflush(stdout);
	}
	return 0;
}