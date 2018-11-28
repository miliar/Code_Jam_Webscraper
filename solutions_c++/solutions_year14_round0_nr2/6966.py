#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <iomanip>

using namespace std;

double cost_to_buy_farm, cokies_produced, target_cookies,time_taken;
int no_farms;


float Time_to_win_with_extra_farm(){

	double next_time;
	next_time = (cost_to_buy_farm / (2 + no_farms*cokies_produced));  // time to buy farm
	no_farms++;
	next_time += (target_cookies / (2 + no_farms*cokies_produced)); //time to win given buying farm
	no_farms--;
	return next_time;

}

int main(int argc, char *argv[]){

	ifstream input;
	ofstream output;

	input.open(argv[1]);
	output.open("./ouput.txt");

	int No_Cases;
	input >> No_Cases;

	for (int i = 0; i < No_Cases; ++i){
		no_farms = 0;
		time_taken = 0;
		bool finished = true;
		input >> cost_to_buy_farm;
		input >> cokies_produced;
		input >> target_cookies;
		while (finished)
		{
			if ((target_cookies / (2 + no_farms*cokies_produced)) > Time_to_win_with_extra_farm()){
				time_taken += (cost_to_buy_farm / (2 + no_farms*cokies_produced)); // time to buy farm
				no_farms++;
			}
			else{
				time_taken += (target_cookies / (2 + no_farms*cokies_produced)); // time to finish
				finished = false;
			}
		}
		output << "Case #" << i + 1 << ": " << setprecision(10) << fixed<< time_taken << endl;

	}
}