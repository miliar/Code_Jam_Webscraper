#include<iostream>
#include<fstream>
#include<vector>
#include<iomanip>
using namespace std;
double cal(double C, double F, double X, double rate) {
	double ans = 0.0000000;
	double cookies = 0.0000000;
	if(C/rate >= X/rate) {
		ans = ans + X/rate;
	} else if(C/rate < X/rate) {
		ans = ans + C/rate;
		rate = rate + F;
		ans += cal(C, F, X, rate);
	}
	return ans;
}


int main() {
ifstream myfile("input.txt");
	int num;
	myfile >> num;
	double C, F, X;
	double rate;
	double ans;
	for(int i = 0; i < num ; i++) {
		rate = 2.0;
		myfile >> C >> F >> X;
		if(C/rate >= X/rate) {
			ans = X/rate;
		} else if(C/rate < X/rate) {
			while((C/rate + (X/(rate+F))) < X/rate) {
				ans = ans + C/rate;
				rate = rate + F;
			}
			ans = ans + X/rate;
		}
		cout << "Case #" << i+1 << ": " << setprecision(9) << ans << endl;
		ans = 0.0;
	}
			
		
		
		
return 0;
}