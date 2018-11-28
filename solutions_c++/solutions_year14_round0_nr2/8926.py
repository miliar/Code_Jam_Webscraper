#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
	int Testcases=0;
	scanf("%d",&Testcases);

	for(int nTestcases=1;nTestcases<=Testcases;nTestcases++)
	{
		double C,F,X;
		scanf("%lf %lf %lf",&C,&F,&X);
		bool keepdoing=true;
		double speed=2;
		double lasttotalseconds=X/speed,totalseconds=0,finaltotalseconds=-1;

		for(int i=0;i<X/C;i++)
		{
			totalseconds+=C/speed;
			speed+=F;
			double temp=totalseconds+(X/speed);
			if(lasttotalseconds<temp){finaltotalseconds=lasttotalseconds;break;}
			else{lasttotalseconds=temp;}
		}

		printf("Case #%d: %.7lf\n",nTestcases,finaltotalseconds);
	}
	return 0;
}
