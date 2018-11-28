#include <iostream>
#include <vector>
#include <iomanip>
#include <cstdlib>

using namespace std;

#define ratio 2.00000;

bool
verifyingCookieFarm (double max_cookies, double cookie_farm_bonus, 
				     double cookie_farm_cost, double total_bonus){

	double result_without_farm, result_with_farm;

	result_without_farm = (max_cookies) / (total_bonus);
	result_with_farm = (cookie_farm_cost / total_bonus) + 
					   ((max_cookies) / (cookie_farm_bonus + total_bonus));

	//cout << "result_without_farm: " << result_without_farm << endl;
	//cout << "result_with_farm: " << result_with_farm << endl << endl; 

	if (result_without_farm < result_with_farm)
		return true;
	
	return false;
}

/***************************************************************************/

int main(){
	int testcases, count = 1;

	double max_cookies, cookie_farm_bonus, cookie_farm_cost;
	double total_bonus, total_time;

	bool b = false;

	cin >> testcases;

	for (int index = 0; index < testcases; index++){
		total_bonus = ratio; 
		total_time = 0.00000;

		b = false;

		cin >> cookie_farm_cost >> cookie_farm_bonus >> max_cookies;

		while (1){
			b = verifyingCookieFarm(max_cookies, cookie_farm_bonus, cookie_farm_cost, total_bonus);

			if (b){
				total_time += (max_cookies / total_bonus);
				break;
			}
			else {
				total_time += (cookie_farm_cost / total_bonus);
				total_bonus += cookie_farm_bonus;
			}

		}

		cout << "Case #" << count << ": " << setiosflags(ios::fixed) << setprecision(7) << 
		         total_time << endl;

		count++;

		/*cout << "cookie farm cost: " << cookie_farm_cost << endl;
		cout << "cookie_farm_bonus: " << cookie_farm_bonus << endl;
		cout << "max_cookies: " << max_cookies << endl;*/


	}

}