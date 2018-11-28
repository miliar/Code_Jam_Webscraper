//#include "cute_algostudy.h"

#include <string>
#include <vector>
#include <iostream>
#include <iomanip>

//namespace code_jam_2014_0_b {

int main(){


	int T;
	std::cin >> T;

	for(int i = 1; i <= T; ++i){

		double C,F,X;
		std::cin >> C >> F >> X;

		double min = X/2.0;
		int buy_fram_cnt = 0;
		double buy_parm_time = 0.0;
		while(true){
			buy_fram_cnt++;
			double time = X/(2.0 + double(buy_fram_cnt)*F);
			buy_parm_time = buy_parm_time + C/(2.0 + double(buy_fram_cnt-1)*F);
			if(time + buy_parm_time >= min){
				break;
			}else{
				min = time + buy_parm_time;
			}
		}

		std::cout << std::fixed << std::setprecision(7);
		std::cout << "Case #" << i << ": " << min << std::endl;
	}

	return 0;
}

//CUTE_MAIN(__FILE__, main);

//}
