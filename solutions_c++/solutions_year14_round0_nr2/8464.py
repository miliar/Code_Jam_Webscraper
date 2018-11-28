#include <iostream>
#include <iomanip>

using namespace std;

void farms(int o){
	cout << "Case #" << o << ": ";

	double t(0.0), g(2.0);
	double C, F, X;
	cin >> C >> F >> X;
	
	bool done(false);

	while(true){
		double t_wo_farm = t + X/g;
		double t_w_farm = t + C/g + X/(g + F);
		if(t_wo_farm < t_w_farm){
			t = t_wo_farm;
			break;
		} else {
			t += C/g;
			g += F;
		}
	}

	cout << t << endl;
}


int main(){
	std::cout << std::setprecision(7) << std::fixed;	
	int T(0);
	cin >> T;
	for(int t(0); t<T; t++)
		farms(t+1);
}
