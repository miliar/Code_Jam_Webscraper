#include <iostream>
#include <iomanip>
#include <cfloat>
int main() {
	double nTc, c, f, x;
	std::cin>>nTc;
	for (int i=0; i<nTc; i++)
	{
		std::cin>>c>>f>>x;
		double cookiePerSec(2);
		double dontBuy(0), buy(0), sec, prevDontBuy(DBL_MAX);
		while (1)
		{
			sec=1/cookiePerSec;
			dontBuy=buy+x*sec;
			buy+=c*sec;
			if (dontBuy>=prevDontBuy)
				break;
			cookiePerSec+=f;
			prevDontBuy=dontBuy;
		}
		std::cout<<"Case #"<<i+1<<": "<<std::setprecision(10)<<std::setiosflags(std::ios::showpoint)<<prevDontBuy<<'\n';
	}
	std::cout<<std::endl;
	return 0;
}