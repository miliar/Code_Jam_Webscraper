#include <iostream>
#include <limits>

using namespace std;
int main(){
	int number_of_cases;
	cin >> number_of_cases;

	cout.precision(std::numeric_limits<double>::digits10);

	for(int i =0; i<number_of_cases; ++i){
		double c;//cost of cookie farm
		double f;//increase in prod_rate by buying a farm
		double x;//cookies to win
		double prod_rate = 2.0;
	
		cin >> c;
		cin >> f;
		cin >> x;

		double time_spent = 0.0;
	while(1){	
		double time_to_farm = c/prod_rate;
		double time_to_win = x/prod_rate;
		double time_to_win_after_farm = x/(prod_rate+f);
	
		if(time_to_win > time_to_win_after_farm+time_to_farm){
			time_spent += time_to_farm;
			prod_rate += f;
		}else{
			time_spent += time_to_win;
			cout << "Case #" << i+1 << ": " << time_spent << endl;
			break;
		}
	}
	}
}
