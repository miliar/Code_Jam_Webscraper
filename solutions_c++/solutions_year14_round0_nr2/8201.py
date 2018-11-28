
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <iomanip>

using namespace std;
#define REP(i, a, b)  for (int i = int(a); i <= int(b); i++) 


int main(){
	
	int test_count;
	cin >> test_count;
	
	REP( test_index , 1 , test_count )
	{
		double C, F, G;
		cin >> C;
		cin >> F;
		cin >> G;
		
		//cout << C << " "<< F << " "<< G << "\n";
									
		double time = 0;
		
		double cookie_rate = 2;
		
		while(1)
		{
			double time_for_target = G/cookie_rate;

			double time_for_target_with_farm = C/cookie_rate + G /( cookie_rate + F);
		
			if( time_for_target > time_for_target_with_farm)
			{
				time = time + 	C/cookie_rate;
				cookie_rate = cookie_rate + F;
			}
			else
			{
				time = time + time_for_target;
				break;
			}
					
			if( G  <= 0 ){
				break;
			}				
		}
		
		cout << "Case #" << test_index <<": "<<std::fixed  <<std::setprecision(7)<< time <<"\n";		
							  											
	}
	
	
	return 0;
}