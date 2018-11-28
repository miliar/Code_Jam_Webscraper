

#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <sstream>

using namespace std;

int toInt(std::string& str){
	int out;
	istringstream stream(str);
	stream >> out;
	return out;	
}

class CookieFarm{
public:
	CookieFarm(double c, double f, double x){
		cost = c;
		speed_up = f;
		target = x;
		time = 0;

	}
	static const int base_rate = 2;
	double cost;
	double speed_up;
	double target;
	double time;
	//double current_rate;
	double get_time(){
		double time = 0;
		double rate = base_rate;
		int n = 1;
		while(true){
		rate = rate + (speed_up * n);
		double if_built = (cost/(rate-speed_up)) + ( target/(rate));
		double not_built = target/(rate-speed_up);
			if(if_built < not_built){
				time += (cost/(rate-speed_up));
			}
			else{
				time += not_built;
				break; //break from while loop
			}
			//cout << time <<endl;
		}
		return time;	
	}
};



int main(){
	//first redirect output to a file
	freopen("large-out.txt", "w", stdout);

	std::string in;
	std::getline(cin,in);
	int numTestCases = toInt(in);
	for(int i = 1; i <= numTestCases ; ++i){
		//read test case
		std::getline(cin,in);
		double temp[3];
		sscanf(in.c_str(), "%lf %lf %lf", temp, temp+1, temp+2);
		CookieFarm ck(temp[0], temp[1], temp[2]);
		double time = ck.get_time();
		//cout << "Case #" << i << ": " << std::setprecision(12) <<  time << endl;
		printf("Case #%d: %.7f\n", i, time);
	}
	//int hi;
	cin.get();

}

