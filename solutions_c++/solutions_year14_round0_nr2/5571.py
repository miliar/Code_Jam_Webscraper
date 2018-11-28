#include <iostream>
using namespace std;

int main(){
	int t; cin >> t;
	for(int ca = 1; ca <= t; ca++){
		double c,f,x;
		cin >> c >> f >> x;
		
		double rate = 2.0;
		double ti = 0;
		
		for(int i=1; true; i++){
			double nti = ti + c/rate;
			if(nti + x/(rate+f) < ti + x/rate){
				ti = nti;
				rate = rate + f;
			}else{
				ti = ti + x/rate;
				break;
			}
		}
		
		cout << "Case #" << ca << ": ";
		cout << std::fixed; cout.precision(9);
		cout << ti;
		cout << endl;
	}
	return 0;
}
