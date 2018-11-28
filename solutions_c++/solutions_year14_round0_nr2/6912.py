#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int T; 
	cin >> T;
	double c, f, x;
	std::cout.precision(7);
	std::cout.setf(std::ios::fixed);
	for(int cas = 1; cas <= T; ++cas){
		cin >> c >> f >> x;
 		double cps = 2;
		double ttx = x/cps;
		double ttxbf = c/cps + x/(cps+f);
		while((ttx > ttxbf)){
			cps+=f;
			ttx = ttxbf; 
			ttxbf -= x/(cps);
			ttxbf += c/cps + x/(cps+f);
		}
		//result is on ttx
		cout << "Case #" << cas << ": " << ttx << endl;
	}
}