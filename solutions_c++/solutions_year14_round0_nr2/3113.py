#include <iostream>
#include <fstream>
#include <vector>
#include <limits.h>
#include <iomanip>
using namespace std;



int main( int argc, char* argv[] ){

	ifstream is;
	is.open(argv[1],std::ifstream::in);

	ofstream os;
	os.open(argv[2],std::ofstream::out);

	int case_total=0;
	double farm_price,cookie_extra, cookie_goal, cookie_total, time=0.0;
	double cookie_rate=2;
	double time_total=0;
	double time_old=0;
	is>>case_total;

	for(int i=0;i<case_total;i++)
	{
		is>>farm_price;
		is>>cookie_extra;
		is>>cookie_goal;
		time_total, time_old, time=0;
		cookie_rate=2.0;
		time_old=cookie_goal/cookie_rate;
		if(cookie_goal<farm_price)
		{
			os<<"Case #"<< i+1 <<": "<<fixed<<setprecision(7)<<time_old<<endl;			
		}
			
		else
		{
			while(true)
			{
				time=time+(farm_price/cookie_rate);
				cookie_rate+=cookie_extra;
			//	os<<cookie_rate<<endl;
			//	os<<"time"<<time<<endl;
				time_total=time+(cookie_goal/cookie_rate);
				if(time_old<time_total)
					break;
				time_old=time_total;
			}
		os<<"Case #"<< i+1 <<": "<<fixed<<setprecision(7)<<time_old<<endl;
		}
		
		
	}
	
	is.close();
	os.close();
return 0;
}
